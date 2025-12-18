"""
QUESTION:
Implement a function named `rotate_cipher` that takes two parameters: `text` (the input string to be decrypted) and `shift` (the number of positions to shift up or down the alphabet). The function should implement a rotation cipher methodology similar to Caesar Cipher and handle uppercase letters, punctuation, and spacing. A negative shift value should rotate to the right in the alphabet. The function should return the decrypted string.
"""

def rotate_cipher(text, shift):
    """
    Function to implement a Caesar cipher on a string.

    Parameters:
    text : str
        The input text string to be encrypted or decrypted.
    shift : int
        The number of positions to shift up or down the alphabet.

    Returns:
    str : 
        The encrypted/decrypted string as output.
    """

    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    len_lowercase = len(lowercase_letters)
    len_uppercase = len(uppercase_letters)

    output = ""

    for char in text:
        if char in lowercase_letters:
            index = lowercase_letters.index(char)
            new_index = (index - shift) % len_lowercase
            output += lowercase_letters[new_index]
        elif char in uppercase_letters:
            index = uppercase_letters.index(char)
            new_index = (index - shift) % len_uppercase
            output += uppercase_letters[new_index]
        else:
            output += char
    return output