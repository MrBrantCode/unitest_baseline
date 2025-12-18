"""
QUESTION:
Create a function `encrypt_message` that takes a string `message` as input and returns the encrypted message using the Caesar Cipher technique with a fixed shift of 3. The function should shift alphabetic characters by 3 places and leave non-alphabetic characters unchanged, wrapping around to the beginning of the alphabet if necessary (e.g., 'z' becomes 'c' and 'Z' becomes 'C').
"""

def caesar_cipher(message):
    encrypted_message = ""
    for i in message:
        if i.isalpha():
            shift = 3
            char_code = ord(i) + shift
            if i.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
            encrypted_message += chr(char_code)
        else:
            encrypted_message += i
    return encrypted_message