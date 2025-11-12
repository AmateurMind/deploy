import streamlit as st
import html
import streamlit.components.v1 as components

st.set_page_config(page_title="PIC Programs", layout="wide")

# Hide the main area watermark and menu
st.markdown("""
    <style>
        
    </style>
""", unsafe_allow_html=True)

PIC_PROGRAMS = {
    "0": r"""
    //0
    //ADD
ORG 0000H
 
 MOV A, #25H      ; First number
 MOV B, #14H      ; Second number
 ADD A, B         ; A = A + B
 MOV R1, A        ; Store result
 END

//SUB
ORG 0000H
 
 MOV A, #25H      ; First number
 MOV B, #14H      ; Second number
 CLR C
 SUBB A, B        ; A = A - B
 MOV R2, A        ; Store result
 
 END
 
//MUL
ORG 0000H
MOV A,#30H
MOV B,#2H
MUL AB
END 
 
//DIV
ORG 0000H
MOV A,#60H
MOV B,#20H
DIV AB
END

//16 BIT ADD
ORG 0000H

; LSB bytes
MOV A, #01H
MOV R1, #05H
ADD A, R1
MOV 30H, A           ; Store LSB result

; MSB bytes
MOV A, #30H
MOV R2, #12H
ADDC A, R2
MOV 31H, A           ; Store MSB result

END


//16 BIT SUB
ORG 0000H

CLR C

; LSB bytes
MOV A, #01H
MOV R1, #05H
SUBB A, R1
MOV 32H, A           ; Store LSB result

; MSB bytes
MOV A, #30H
MOV R2, #12H
SUBB A, R2
MOV 33H, A           ; Store MSB result

END

//ADD BCD
ORG 0000H

MOV A, #45H      ; BCD number 1
MOV B, #38H      ; BCD number 2
ADD A, B
DA A             ; Decimal adjust
MOV R4, A        ; Store correct BCD result

END

//PACKED BCD TO UNPACKED
ORG 0000H

MOV A, #58H         ; Packed BCD

; Lower nibble
ANL A, #0FH
MOV R1, A

; Upper nibble
MOV A, #58H
ANL A, #0F0H
SWAP A
MOV R2, A

END

//count number of 0's and 1's
ORG 0000H

MOV A, #97H        ; Example 8-bit number
MOV R7, #08H       ; Loop counter for 8 bits
MOV R2, #00H       ; Zero counter
MOV R3, #00H       ; One counter

BACK:
    JB ACC.0, ONE  ; If ACC.0 = 1, jump to ONE
    INC R2         ; Otherwise zero++ 
    SJMP NEXT

ONE:
    INC R3         ; One++

NEXT:
    RR A           ; Rotate right (next bit moves into ACC.0)
    DJNZ R7, BACK  ; Repeat for all 8 bits

SJMP $
END

""",
    "1": r"""
//1
//move internal ram to gen purpose ram MICRO
ORG 0000H
 
 MOV 35H, #'M'
 MOV 36H, #'I'
 MOV 37H, #'C'
 MOV 38H, #'R'
 MOV 39H, #'O'
 
 MOV R0, #35H     ; Source starting address (35H)
 MOV R1, #60H     ; Destination starting address (60H)
 MOV R2, #05H     ; Number of bytes to transfer (5 characters)
 
 L:  MOV A, @R0    ; Move data from source (address in R0) to Accumulator
     MOV @R1, A    ; Move data from Accumulator to destination (address in R1)
     INC R0        ; Increment source pointer
     INC R1        ; Increment destination pointer
     DJNZ R2, L    ; Decrement R2 and repeat until all bytes are moved
 
 END

//move from external to internal in external ram give 1,2,3,4,5 next to 20 then check internal ram 
        ORG 0000H
 
         MOV DPTR, #0020H   ; DPTR -> external memory source address 0020H
         MOV R0,   #45H     ; R0 -> internal RAM destination starting at 45H
         MOV R2,   #06H     ; R2 -> byte counter (6 bytes to copy)
 
 BACK:   MOVX A, @DPTR      ; Read a byte from external memory [DPTR] -> A
         MOV  @R0, A        ; Write A into internal RAM at address in R0
         INC  DPTR          ; Next byte in external memory
         INC  R0            ; Next location in internal RAM
         DJNZ R2, BACK      ; Decrement R2; if not zero jump back to BACK
 
         END
 
//store str MODERN on rom 200h internal ram reverse it
ORG 0000H

MOV DPTR, #0200H   ; ROM location of the word "MODERN"
MOV R0,   #40H     ; Start address in internal RAM
MOV R1,   #06H     ; Number of characters (6)
CLR A

L1: CLR A
    MOVC A, @A+DPTR   ; Read a character from ROM
    MOV @R0, A        ; Store it in RAM
    PUSH ACC          ; Push it to stack (for reversal)
    INC DPTR          ; Next ROM address
    INC R0            ; Next RAM address
    DJNZ R1, L1       ; Loop till all bytes copied

MOV R0, #50H          ; Destination for reversed string
MOV R1, #06H          ; Number of characters to pop

L2: POP ACC            ; Pop last character from stack
    MOV @R0, A         ; Store reversed order in RAM
    INC R0
    DJNZ R1, L2        ; Repeat for all 6 chars

ORG 0200H
DB 'MODERN'            ; Data stored in code memory

END
""",
"2": r"""
//2
    //1.WAP to flash LEDS on P2
#include <REG51.H>

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    while(1) {
        P2 = 0x00;      // Turn OFF all LEDs connected to Port 2
        delay(500);     // Wait for 500 ms
        P2 = 0xFF;      // Turn ON all LEDs connected to Port 2
        delay(500);     // Wait for 500 ms
    }
}


//2.WAP to generate rotational pattern on P1
#include <REG51.H>

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    unsigned char x = 0x01;  // Start with the first LED ON
    while(1) {
        P1 = x;              // Output value to Port 1
        delay(500);          // Wait 500 ms
        x = x << 1;          // Shift left (next LED ON)
        if(x == 0x00) {      // When all LEDs have shifted off
            x = 0x01;        // Reset back to first LED
        }
    }
}



//3.WAp to generate zifzag pattern on p2
#include <REG51.H>

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    while(1) {
        P2 = 0xAA;     // 10101010 pattern – alternate LEDs ON/OFF
        delay(500);    // Wait for 500 ms
        P2 = 0x55;     // 01010101 pattern – opposite LEDs ON/OFF
        delay(500);    // Wait for 500 ms
    }
}



//4.WAP to count BCD numbers
#include <REG51.H>

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    unsigned char bcd;
    while(1) {
        for(bcd = 0; bcd < 9; bcd++) {
            P2 = bcd;        // Output BCD value to Port 2
            delay(1000);     // 1-second delay
        }
    }
}



//5.WAP to count HEX(0 TO f)
#include <REG51.H>

unsigned char str[16] = {
    0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07,
    0x7F, 0x6F, 0x3F, 0x7C, 0x39, 0x5E, 0x79, 0x71
};

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    unsigned char i;
    while(1) {
        for(i = 0; i < 16; i++) {
            P2 = str[i];     // Output pattern to Port 2
            delay(500);      // Wait for 500 ms
        }
    }
}



//6.COUNT NUMBER 1 TO 12
#include <REG51.H>

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    unsigned char count = 0;
    while(1) {
        P2 = count;       // Send count value to Port 2
        delay(500);       // 500 ms delay
        count++;          // Increment count
        if(count >= 10)   // If count exceeds 9
            count = 0;    // Reset back to 0
    }
}



//7.DISPLAY MICRO
#include <REG51.H>

unsigned char str[5] = {'M', 'I', 'C', 'R', 'O'};

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    unsigned char i;
    while(1) {
        for(i = 0; i < 5; i++) {
            P2 = str[i];     // Send each character to Port 2
            delay(500);      // Wait for 500 ms
        }
    }
}


""",
"3": r"""
//3
//1.CLOCKWISE STEPPER
#include <REG51.H>

unsigned char step_sequence[4] = {0x01, 0x02, 0x04, 0x08};

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    unsigned int i;
    while(1) {
        for(i = 0; i < 4; i++) {
            P1 = step_sequence[i];  // Send step pattern to Port 1
            delay(5000);            // Delay between steps
        }
    }
}

//2.ANTICLOCKWISE
#include <REG51.H>

unsigned char step_sequence[4] = {0x08, 0x04, 0x02, 0x01};

void delay(unsigned int ms) {
    unsigned int i, j;
    for(i = 0; i < ms; i++) {
        for(j = 0; j < 1257; j++);
    }
}

void main(void) {
    unsigned int i;
    while(1) {
        for(i = 0; i < 4; i++) {
            P1 = step_sequence[i];  // Send step pattern to Port 1
            delay(5000);            // Delay between steps
        }
    }
}
""",
    "4": r"""
//4



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
//6


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
//7


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
//8


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
    <button style='position:absolute;top:8px;left:8px;padding:6px 10px;border-radius:4px;border:none;background:#007bff;color:#fff;cursor:pointer;z-index:2;font-weight:600;display:inline-flex;align-items:center;gap:4px;' 
        onclick="(() => {{
            const btn = event.target;
            const text = document.getElementById('{pre_id}').innerText;
            navigator.clipboard.writeText(text)
                .then(() => {{
                    btn.innerHTML = '✓ Copied';
                    setTimeout(() => btn.innerHTML = 'Copy', 1000);
                }})
                .catch(err => alert('Failed to copy: ' + err));
        }})()">Copy</button>
    <pre id='{pre_id}' style='white-space:pre-wrap;font-family:monospace;margin-top:36px;max-height:500px;overflow-y:auto;'>{esc}</pre>
</div>
""",height=700)

# Keep the download button but hide code display
if sel:
    st.download_button("Download", code, file_name=sel+".c")
