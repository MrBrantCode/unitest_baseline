"""
QUESTION:
Create a function `shift_encrypt` to encrypt a given text by shifting each character by a specified number of steps, and a function `shift_decrypt` to decrypt the encrypted text back to its original form. The function should handle both uppercase and lowercase characters, but may not work well with punctuation. Use a Caesar Cipher with a shift of 5 steps for this problem. The input text is "Greetings, Universe!" and the shift is 5.
"""

def shift_encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)

        else:
            result += char

    return result


def shift_decrypt(encrypted_text, s):
    result = ""

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)

        else:
            result += char

    return result