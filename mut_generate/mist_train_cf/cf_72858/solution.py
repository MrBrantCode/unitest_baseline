"""
QUESTION:
Implement a function to encrypt and decrypt a string using a Caesar cipher. The function should take two parameters: the input text and a shift key of any integer number. It should preserve the case of the original letters and keep non-alphabet characters unchanged.
"""

def caesar_cipher(text, shift):
    result = ""
    for i in text:
        if i.isalpha():
            shift_temp = 97 if i.islower() else 65
            if shift > 0:  # encryption
                i = chr((ord(i) + shift - shift_temp) % 26 + shift_temp)
            else:  # decryption
                i = chr((ord(i) - abs(shift) - shift_temp) % 26 + shift_temp)
        result += i
    return result