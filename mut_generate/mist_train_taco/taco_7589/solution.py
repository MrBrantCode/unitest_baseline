"""
QUESTION:
Caesar Cipher is one of the earliest and simplest encryption technique.
To encrypt a message, we shift the alphabets of the message by a fixed position or key. 

For example, if message is ABC , and we shift each character by 3 characters, we will get  DEF. Here key is 3.

Given a message and key , compute its Caesar Cipher.

Input
First line contains t - number of test cases.
2* t lines follow

First line of each test case contains k, the key of the Cipher.

Second line of each test case contains the message

Output
Print encrypted message for each test case in a separate line.

Constraints
1 < t ≤ 1000
0 < k ≤ 1000

SAMPLE INPUT
3
2
x
3
oXyh
2
nn

SAMPLE OUTPUT
z
rAbk
pp
"""

def caesar_cipher(message: str, key: int) -> str:
    encrypted_message = ''
    for char in message:
        if 'a' <= char <= 'z':
            encrypted_message += chr((ord(char) + key - ord('a')) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_message += chr((ord(char) + key - ord('A')) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message