"""
QUESTION:
Write a function named `modified_caesar_cipher` that takes two parameters: a string `text` and an integer `shift`. The function should reverse the order of the letters in the text and then shift each letter by the ASCII value of the previous letter in the alphabet (i.e., shift 'a' by 1, 'b' by 2, etc.). The function should return the encrypted text as a string. Assume the input text only contains lowercase letters.
"""

def modified_caesar_cipher(text, shift):
    reversed_text = text[::-1]  
    encrypted_text = ""
    for i, letter in enumerate(reversed_text):
        shift_amount = ord(reversed_text[(i-1) % len(reversed_text)]) - 96  # Shift each letter by the ASCII value of the previous letter
        ascii_value = ord(letter) + shift_amount  
        encrypted_text += chr(ascii_value)
    return encrypted_text