"""
QUESTION:
Implement a function `caeser_encrypt(text, shifts)` and its inverse `caeser_decrypt(text, shifts)` that use a sequence of shift values to encrypt and decrypt a text string. The function should take a text string and a list of numbers as arguments, where the list of numbers serves as the sequence of shift values. Apply each shift value in the list to each corresponding character in the string, looping back to the start of the list when the end is reached. Handle spaces and punctuation by leaving them untouched, and maintain case sensitivity. If a shift goes past 'z' or 'Z', loop back to the start of the alphabet.
"""

def caeser_encrypt(text, shifts):
    encrypted_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = alphabet.upper()
    shift_len = len(shifts)
    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            encrypted_text += alphabet[(alphabet.index(char) + shifts[i%shift_len]) % 26]
        elif char in ALPHABET:
            encrypted_text += ALPHABET[(ALPHABET.index(char) + shifts[i%shift_len]) % 26]
        else:
            encrypted_text += char  
    return encrypted_text


def caeser_decrypt(text, shifts):
    decrypted_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = alphabet.upper()
    shift_len = len(shifts)
    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            decrypted_text += alphabet[(alphabet.index(char) - shifts[i%shift_len]) % 26]
        elif char in ALPHABET:
            decrypted_text += ALPHABET[(ALPHABET.index(char) - shifts[i%shift_len]) % 26]
        else:
            decrypted_text += char  
    return decrypted_text