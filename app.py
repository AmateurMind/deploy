import streamlit as st
import html
import streamlit.components.v1 as components

st.set_page_config(page_title="PIC Programs", layout="wide")

# Hide the main area watermark and menu
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

PIC_PROGRAMS = {
    "4": r"""
#include <p18f4520.h>
#include <delays.h>

#pragma config OSC = HS
#pragma config WDT = OFF
#pragma config LVP = OFF
#pragma config PBADEN = OFF

#define BUZZER PORTAbits.RA3
#define SWITCH0 PORTBbits.RB0
#define SWITCH1 PORTBbits.RB1

void main(void)
{
    TRISA = 0x00;
    TRISB = 0xFF;
    TRISD = 0x00;

    PORTD = 0xFF;
    BUZZER = 0x00;

    while(1)
    {
        if(SWITCH0 == 0)
        {
            while(1)
            {
                BUZZER = 1;
                PORTD = 0x37;
                Delay10KTCYx(100);
                PORTD = 0x3B;
                Delay10KTCYx(100);
                PORTD = 0x3D;
                Delay10KTCYx(100);
                PORTD = 0x3E;
                Delay10KTCYx(100);

                if(SWITCH1 == 0)
                    break;
            }
        }
        else if(SWITCH1 == 0)
        {
            while(1)
            {
                BUZZER = 0;
                PORTD = 0xCE;
                Delay10KTCYx(100);
                PORTD = 0xCD;
                Delay10KTCYx(100);
                PORTD = 0xCB;
                Delay10KTCYx(100);
                PORTD = 0xC7;
                Delay10KTCYx(100);

                if(SWITCH0 == 0)
                    break;
            }
        }
    }
}
""",

    

    "6": r"""
#include <p18f4520.h>
#include <delays.h>

#pragma config OSC = HS
#pragma config WDT = OFF
#pragma config LVP = OFF
#pragma config PBADEN = OFF

#define BUZZER PORTAbits.RA3

unsigned char TimerOnflag = 0;

void Timer0Init(void)
{
    T0CON = 0x87;
    TMR0H = 0xB3;
    TMR0L = 0xB4;

    RCONbits.IPEN = 1;
    INTCON = 0xE0;
    INTCON2bits.TMR0IP = 1;
}

void TMRISR(void);

#pragma code InterruptVectorHigh = 0x08
void InterruptVectorHigh(void)
{
    _asm
        goto TMRISR
    _endasm
}
#pragma code

#pragma interrupt TMRISR
void TMRISR(void)
{
    if (INTCONbits.TMR0IF == 1)
    {
        INTCONbits.TMR0IF = 0;
        TMR0H = 0xB3;
        TMR0L = 0xB4;

        if (TimerOnflag)
        {
            PORTD = 0x00;
            TimerOnflag = 0;
            BUZZER = 0;
            Delay10KTCYx(700);
        }
        else
        {
            PORTD = 0xFF;
            TimerOnflag = 1;
            BUZZER = 0;
            Delay10KTCYx(700);
        }
    }
}

void main(void)
{
    Timer0Init();
    TimerOnflag = 0;

    TRISD = 0x00;
    PORTD = 0x00;
    TRISAbits.TRISA3 = 0;

    while (1)
    {
        BUZZER = 1;
    }
}

""",

    "7_Serial": r"""
#include <p18f4520.h>
#include <stdio.h>
#include <delays.h>

#pragma config OSC = HS
#pragma config WDT = OFF
#pragma config LVP = OFF

void InitUSART(void)
{
    TRISCbits.TRISC6 = 1;   // TX pin input (required for UART module)
    TRISCbits.TRISC7 = 1;   // RX pin input

    SPBRG = 31;             // 9600 baud @ 20 MHz
    TXSTA = 0x20;           // Enable transmitter, async mode
    RCSTAbits.SPEN = 1;     // Enable serial port
    RCSTAbits.CREN = 1;     // Continuous receive enable
}

// IMPORTANT: C18 printf expects a function named putch()
void putch(unsigned char ch)
{
    while (!PIR1bits.TXIF);   // Wait until TXREG is empty
    TXREG = ch;
}

unsigned char getchar(void)
{
    while (!PIR1bits.RCIF);   // Wait for received character
    return RCREG;
}

void main(void)
{
    InitUSART();

    printf("Hello PIC18F4520!\r\n");

    while (1)
    {
        putch(getchar());    // Echo UART input
    }
}

""",

    "8_PWM": r"""
#include <p18f4520.h>
#include <delays.h>

#pragma config OSC = HS
#pragma config WDT = OFF
#pragma config LVP = OFF
#pragma config PBADEN = OFF

void main(void)
{
    unsigned char dc;

    TRISC = 0;
    PORTC = 0;

    PR2 = 0b01111100;
    T2CON = 0b00000101;
    CCP1CON = 0b00001100;
    CCP2CON = 0b00111100;

    for (;;)
    {
        for (dc = 0; dc < 128; dc++)
        {
            CCPR1L = dc;
            CCPR2L = 128 - dc;
            Delay10KTCYx(50);
        }

        for (dc = 127; dc > 0; dc--)
        {
            CCPR1L = dc;
            CCPR2L = 128 - dc;
            Delay10KTCYx(50);
        }
    }
}

"""
}

st.sidebar.title("-")
sel = st.sidebar.radio("Select", list(PIC_PROGRAMS.keys()))
code = PIC_PROGRAMS[sel]

# Create a JS-safe version of the raw code to copy via clipboard (escape backticks and backslashes)
js_safe = code.replace('\\','\\\\').replace('`','\\`')

# Persistent copy button in the sidebar — always available and will copy the raw code even if the
# main code panel is not visible.
with st.sidebar:
    components.html(f"""
    <div style='padding:6px;display:flex;justify-content:flex-end;'>
        <button style='padding:6px 10px;border-radius:4px;border:none;background:#28a745;color:#fff;cursor:pointer;font-weight:600;' onclick="navigator.clipboard.writeText(`{js_safe}`)">Copy</button>
    </div>
    """, height=60)

pre_id = f"code_{abs(hash(sel))}"
esc = html.escape(code)
components.html(f"""
<div style='background:#f1f1f1;padding:10px;border-radius:6px;position:relative;'>
    <button style='position:absolute;top:8px;right:8px;padding:6px 10px;border-radius:4px;border:none;background:#007bff;color:#fff;cursor:pointer;z-index:2;font-weight:600;' onclick="navigator.clipboard.writeText(document.getElementById('{pre_id}').innerText)">Copy</button>
    <pre id='{pre_id}' style='white-space:pre-wrap;font-family:monospace;margin-top:36px;'>{esc}</pre>
</div>
""",height=40)

# Keep the download button but hide code display
if sel:
    st.download_button("Download", code, file_name=sel+".c")
