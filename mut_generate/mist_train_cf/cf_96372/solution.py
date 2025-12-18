"""
QUESTION:
Develop a function named `caesar_cipher_encode` that takes two parameters: a text string and a shift value. The function should encode the text string using the Caesar cipher with the variable shift, handling special characters, numbers, and maintaining their original positions in the encoded string. The function should also wrap around the alphabet and correctly encode both uppercase and lowercase letters. The implementation should be optimized for both efficiency and readability.
"""

def caesar_cipher_encode(text, shift):
    # Create a list of lowercase and uppercase letters
    lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    
    # Initialize the encoded text
    encoded_text = ''
    
    # Iterate over each character in the text
    for char in text:
        if char.islower():
            # Encode lowercase letters
            index = lowercase_letters.index(char)
            encoded_index = (index + shift) % 26
            encoded_text += lowercase_letters[encoded_index]
        elif char.isupper():
            # Encode uppercase letters
            index = uppercase_letters.index(char)
            encoded_index = (index + shift) % 26
            encoded_text += uppercase_letters[encoded_index]
        else:
            # Preserve special characters and numbers
            encoded_text += char
    
    return encoded_text