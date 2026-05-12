import streamlit as st
import html
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="PIC Programs", layout="wide")

# Hide the main area watermark and menu
st.markdown("""
    <style>
        
    </style>
""", unsafe_allow_html=True)

# Image paths for interfacing diagrams
image_paths = ["2exp.jpg", "3exp.jpg", "PIC_page-0003.jpg", "PIC_page-0004.jpg", "PIC_page-0005.jpg", "PIC_page-0006.jpg", "PIC_page-0007.jpg", "PIC_page-0008.jpg"]

PIC_PROGRAMS = {
    
    "EXP1": r"""Program:-1.
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char password[100];
    int hasUpper, hasLower, hasDigit, hasSpecial;
    int score;
    while(1)
    {
        printf("\nEnter password (minimum 8 characters): ");
        scanf("%s", password);
        int length = strlen(password);
        hasUpper = hasLower = hasDigit = hasSpecial = 0;
        score = 0;
        if(length >= 8)
            score += 20;
        for(int i = 0; i < length; i++)
        {
            if(isupper(password[i]))
                hasUpper = 1;
            else if(islower(password[i]))
                hasLower = 1;
            else if(isdigit(password[i]))
                hasDigit = 1;
            else
                hasSpecial = 1;
        }
        if(hasUpper)
            score += 20;
        if(hasLower)
            score += 20;
        if(hasDigit)
            score += 20;
        if(hasSpecial)
            score += 20;
        printf("Password Strength: %d%%\n", score);
        if(score == 100)
        {
            printf("Strong Password Accepted!\n");
            break;
        }
        else
        {
            printf("Weak Password! Re-enter again.\n");
        }
    }
    return 0;
}











2.Printed password:

#include <stdio.h>
#include <string.h>

int main()
{
    char entered[50];
    char newpass[50];
    char password[50] = "admin123";   // Default password
    int attempts = 0;

    printf("Default Password is: %s\n", password);

    while(attempts < 3)
    {
        printf("\nEnter Default Password: ");
        scanf("%s", entered);

        if(strcmp(entered, password) == 0)
        {
            printf("Login Successful!\n");
            while(1)
            {
                printf("Enter New Password (min 8 characters): ");
                scanf("%s", newpass);

                if(strlen(newpass) >= 8)
                {
                    strcpy(password, newpass);
                    printf("Password Changed Successfully!\n");
                    break;
                }
                else
                {
                    printf("Password too short! Try again.\n");
                }
            }
            printf("\nLogin again with New Password\n");
            printf("Enter Password: ");
            scanf("%s", entered);

            if(strcmp(entered, password) == 0)
            {
                printf("Login Successful with New Password!\n");
            }
            else
            {
                printf("Wrong New Password!\n");
            }
            return 0;
        }
        else
        {
            attempts++;
            printf("Wrong Password! Attempts left: %d\n", 3 - attempts);
        }
    }
    printf("Too many wrong attempts! Access Denied.\n");
    return 0;
}

3.Printed password:
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string password;
    cout << "Enter password: ";
    cin >> password;
    cout << "Your password is: " << password << endl;
    cout << "\nWarning: Printing passwords in plain text is insecure!\n";

    return 0;
}

4.Transmitting password:

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string password;
    cout << "Enter password to transmit: ";
    cin >> password;
    string transmittedData = password;   // insecure transmission
    cout << "Password transmitted: " << transmittedData << endl;
    cout << "\nWarning: Transmitting passwords in plain text is insecure! Use encryption instead.\n";
    return 0;
}

""",
    "EXP2 ": r"""#include <stdio.h>
#include <ctype.h>
#include <string.h>

void encrypt(char text[], int key)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isupper(text[i]))
        {
            text[i] = ((text[i] - 'A' + key) % 26) + 'A';
        }
        else if (islower(text[i]))
        {
            text[i] = ((text[i] - 'a' + key) % 26) + 'a';
        }
    }
}
void decrypt(char text[], int key)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isupper(text[i]))
        {
            text[i] = ((text[i] - 'A' - key + 26) % 26) + 'A';
        }
        else if (islower(text[i]))
        {
            text[i] = ((text[i] - 'a' - key + 26) % 26) + 'a';
        }
    }
}
int main()
{
    char text[100];
    int key;
    char choice;
    printf("Enter message: ");
    fgets(text, sizeof(text), stdin);
    printf("Enter key: ");
    scanf("%d", &key);

    key = key % 26;   // Reduce key if greater than 26

    printf("Type E to encrypt or D to decrypt: ");
    scanf(" %c", &choice);
    if (choice == 'E' || choice == 'e')
    {
        encrypt(text, key);
        printf("Encrypted message: %s", text);
    }
    else if (choice == 'D' || choice == 'd')
    {
        decrypt(text, key);
        printf("Decrypted message: %s", text);
    }
    else
    {
        printf("Invalid choice!\n");
    }
    return 0;
}


""",
"EXP3": r"""Ceasar Cipher:
#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define KEY 3
int main()
{
    char plain[100];
    char cipher[100];

    printf("Enter Plain Text: ");
    fgets(plain, sizeof(plain), stdin);

    strcpy(cipher, plain);

    for (int i = 0; cipher[i] != '\0'; i++)
    {
        if (isupper(cipher[i]))
        {
            cipher[i] = ((cipher[i] - 'A' + KEY) % 26) + 'A';
        }
        else if (islower(cipher[i]))
        {
            cipher[i] = ((cipher[i] - 'a' + KEY) % 26) + 'a';
        }
    }
    printf("\nPlain Text : %s", plain);
    printf("Cipher Text : %s", cipher);
    return 0;
}
Substitution Cipher:
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main()
{
    char plain[100];
    char cipher[100];
    char key[] = "1Q!2W@3E#4R$5T%6Y7U&8I9O0P";

    printf("Enter Plain Text: ");
    fgets(plain, sizeof(plain), stdin);

    strcpy(cipher, plain);

    for (int i = 0; cipher[i] != '\0'; i++)
    {
        if (isupper(cipher[i]))
        {
            cipher[i] = key[cipher[i] - 'A'];
        }
        else if (islower(cipher[i]))
        {
            cipher[i] = tolower(key[cipher[i] - 'a']);
        }
    }
    printf("\nPlain Text : %s", plain);
    printf("Cipher Text : %s", cipher);
    return 0;
}
Trasposition Cipher: 
1.Reverse the plain text:
#include <stdio.h>
#include <string.h>

int main()
{
    char plain[100];
    char cipher[100];
    int len;

    printf("Enter Plain Text: ");
    fgets(plain, sizeof(plain), stdin);

    len = strlen(plain);

    if (plain[len - 1] == '\n')
    {
        plain[len - 1] = '\0';
        len--;
    }

    for (int i = 0; i < len; i++)
    {
        cipher[i] = plain[len - 1 - i];
    }
    cipher[len] = '\0';
    printf("\nPlain Text : %s\n", plain);
    printf("Cipher Text : %s\n", cipher);
    return 0;
}
2.Group of 2 alphabets:
#include <stdio.h>
#include <string.h>
int main()
{
    char plain[100];
    char cipher[100];
    int len, index = 0;
    printf("Enter Plain Text: ");
    fgets(plain, sizeof(plain), stdin);
    len = strlen(plain);
    if (plain[len - 1] == '\n')
    {
        plain[len - 1] = '\0';
        len--;
    }
    for (int i = len - 2; i >= 0; i -= 2)
    {
        cipher[index++] = plain[i];
        if (i + 1 < len)
            cipher[index++] = plain[i + 1];
    }
    if (len % 2 != 0)
    {
        cipher[index++] = plain[0];
    }
    cipher[index] = '\0';
    printf("\nPlain Text : %s\n", plain);
    printf("Cipher Text : %s\n", cipher);
    return 0;
}
3.Group of 3 alphabets:
#include <stdio.h>
#include <string.h>

int main()
{
    char plain[100];
    char cipher[100];
    int len, index = 0;
    printf("Enter Plain Text: ");
    fgets(plain, sizeof(plain), stdin);
    len = strlen(plain);
    if (plain[len - 1] == '\n')
    {
        plain[len - 1] = '\0';
        len--;
    }
    for (int i = len - 3; i >= 0; i -= 3)
    {
        for (int j = 0; j < 3 && (i + j) < len; j++)
        {
            cipher[index++] = plain[i + j];
        }
    }
    int remainder = len % 3;
    if (remainder != 0)
    {
        for (int i = 0; i < remainder; i++)
        {
            cipher[index++] = plain[i];
        }
    }
    cipher[index] = '\0';
    printf("\nPlain Text : %s\n", plain);
    printf("Cipher Text : %s\n", cipher);

    return 0;
}

""",
    "EXP5": r"""
Exp-05
Code 1 
#include <iostream>
#include <string>
using namespace std;

string encrypt(string text, string key) {
    string output = text;
    for(int i = 0; i < text.length(); i++)
        output[i] = text[i] ^ key[i % key.length()];
    return output;
}

int main() {
    cout << "Message Encryption Using DES Algorithm\n";
    cout << "-------\n";

    string message = "NETWORK SECURITY";
    string key = "mydeskey";

    cout << "Message [Byte Format] : [B@" << (void*)message.c_str() << endl;
    cout << "Message : " << message << endl;

    string encrypted = encrypt(message, key);
    cout << "Encrypted Message: [B@" << (void*)encrypted.c_str() << endl;

    string decrypted = encrypt(encrypted, key);
    cout << "Decrypted Message: " << decrypted << endl;

    return 0;
}
Code 02

 #include <iostream>
using namespace std;

int gcd(int e, int z) {
    if(e == 0) return z;
    else return gcd(z % e, e);
}

long long modPow(long long base, long long exp, long long mod) {
    long long result = 1;
    base = base % mod;
    while(exp > 0) {
        if(exp % 2 == 1) result = (result * base) % mod;
        exp = exp / 2;
        base = (base * base) % mod;
    }
    return result;
}

int main() {
    int p = 11, q = 13, n, z, d = 0, e, i;
    int msg = 12;

    n = p * q;
    z = (p - 1) * (q - 1);
    cout << "the value of z = " << z << endl;

    for(e = 2; e < z; e++)
        if(gcd(e, z) == 1) { break; }

    cout << "the value of e = " << e << endl;

    for(i = 1; d == 0; i++)
        if((i * z + 1) % e == 0) d = (i * z + 1) / e;

    cout << "the value of d = " << d << endl;

    long long encrypted = modPow(msg, e, n);
    long long decrypted = modPow(encrypted, d, n);

    cout << "Original:  " << msg << endl;
    cout << "Encrypted: " << encrypted << endl;
    cout << "Decrypted: " << decrypted << endl;

    return 0;
}




    """,

    

    "exp6": r"""Exp06
#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "Message Encryption Using DES Algorithm (Simulation)\n\n";

    string text = "Samiksha Gumphekar";
    cout << "Message: " << text << endl;

    int key = 5;

    string encrypted = text;
    for(int i = 0; i < text.length(); i++)
        encrypted[i] = text[i] ^ key;

    cout << "Encrypted Message: ";
    for(char c : encrypted)
        cout << c;
    cout << endl;

    string decrypted = encrypted;
    for(int i = 0; i < encrypted.length(); i++)
        decrypted[i] = encrypted[i] ^ key;

    cout << "Decrypted Message: " << decrypted << endl;

    return 0;
}

""",

    "exp7": r"""#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef unsigned char uint8;

#define Nb 4
#define Nk 8
#define Nr 14

static const uint8 sbox[256] = {
0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16
};

uint8 Rcon[15] = {
    0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36
};

uint8 xtime(uint8 x)
{
    return (x << 1) ^ ((x >> 7) * 0x1b);
}

void SubBytes(uint8 state[4][4])
{
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            state[i][j] = sbox[state[i][j]];
}

void ShiftRows(uint8 state[4][4])
{
    uint8 temp;

    temp = state[1][0];
    state[1][0] = state[1][1];
    state[1][1] = state[1][2];
    state[1][2] = state[1][3];
    state[1][3] = temp;

    uint8 temp1 = state[2][0];
    uint8 temp2 = state[2][1];
    state[2][0] = state[2][2];
    state[2][1] = state[2][3];
    state[2][2] = temp1;
    state[2][3] = temp2;

    temp = state[3][3];
    state[3][3] = state[3][2];
    state[3][2] = state[3][1];
    state[3][1] = state[3][0];
    state[3][0] = temp;
}

void MixColumns(uint8 state[4][4])
{
    for(int i = 0; i < 4; i++)
    {
        uint8 a = state[0][i];
        uint8 b = state[1][i];
        uint8 c = state[2][i];
        uint8 d = state[3][i];

        state[0][i] = xtime(a) ^ xtime(b) ^ b ^ c ^ d;
        state[1][i] = a ^ xtime(b) ^ xtime(c) ^ c ^ d;
        state[2][i] = a ^ b ^ xtime(c) ^ xtime(d) ^ d;
        state[3][i] = xtime(a) ^ a ^ b ^ c ^ xtime(d);
    }
}

void AddRoundKey(uint8 state[4][4], uint8* roundKey)
{
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            state[j][i] ^= roundKey[i * 4 + j];
}

void KeyExpansion(uint8* key, uint8* roundKey)
{
    memcpy(roundKey, key, 32);

    uint8 temp[4];
    int i = 8;

    while(i < 4 * (Nr + 1))
    {
        for(int j = 0; j < 4; j++)
            temp[j] = roundKey[(i - 1) * 4 + j];

        if(i % Nk == 0)
        {
            uint8 k = temp[0];

            temp[0] = sbox[temp[1]] ^ Rcon[i / Nk];
            temp[1] = sbox[temp[2]];
            temp[2] = sbox[temp[3]];
            temp[3] = sbox[k];
        }
        else if(i % Nk == 4)
        {
            for(int j = 0; j < 4; j++)
                temp[j] = sbox[temp[j]];
        }

        for(int j = 0; j < 4; j++)
            roundKey[i * 4 + j] = roundKey[(i - Nk) * 4 + j] ^ temp[j];

        i++;
    }
}

void AES256Encrypt(uint8* input, uint8* key, uint8* output)
{
    uint8 state[4][4];
    uint8 roundKey[240];

    KeyExpansion(key, roundKey);

    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            state[j][i] = input[i * 4 + j];

    AddRoundKey(state, roundKey);

    for(int round = 1; round < Nr; round++)
    {
        SubBytes(state);
        ShiftRows(state);
        MixColumns(state);
        AddRoundKey(state, roundKey + round * 16);
    }

    SubBytes(state);
    ShiftRows(state);
    AddRoundKey(state, roundKey + Nr * 16);

    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            output[i * 4 + j] = state[j][i];
}

int main()
{
    uint8 key[32] = {0};
    uint8 plaintext[16] = {0};
    uint8 ciphertext[16];

    AES256Encrypt(plaintext, key, ciphertext);

    cout << "Cipher Text: ";

    for(int i = 0; i < 16; i++)
        printf("%02x ", ciphertext[i]);

    return 0;
}


""",
    "exp8": r"""Exp08
Hashmap only runs in online complier
Python code 

import hashlib

def get_md5(input_text):
    md5_hash = hashlib.md5()
    md5_hash.update(input_text.encode())
    return md5_hash.hexdigest()

s = "samikshagumphekar"
print("Your HashCode Generated by MD5 is:", get_md5(s))
"""

}

st.sidebar.title("Shhhhhhhh!!")
sel = st.sidebar.radio("Select", list(PIC_PROGRAMS.keys()))

# Show code for selections
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
