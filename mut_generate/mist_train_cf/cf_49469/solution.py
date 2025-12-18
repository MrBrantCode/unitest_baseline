"""
QUESTION:
Design a function named `caesar_cipher` that takes a string `str_to_encrypt` and an integer `shift` as input, and returns the encrypted string using the Caesar Cipher algorithm. The function should handle alphanumeric sequences, preserve the original casing of letters, and have a time complexity of O(n) to match the standards set by Big O notation.
"""

def caesar_cipher(str_to_encrypt, shift):
    encrypted_str = ""
    
    for char in str_to_encrypt:
        if char.isalpha():
            # Check if character is upper case
            is_upper_case = char.isupper()
            
            # Obtain ASCII value
            char = ord(char.lower())
            
            # Shift the character
            char = (char + shift - 97) % 26 + 97
            
            # Convert it back to its original casing
            if is_upper_case:
                char = chr(char).upper()
            else:
                char = chr(char)
        encrypted_str += char
        
    return encrypted_str