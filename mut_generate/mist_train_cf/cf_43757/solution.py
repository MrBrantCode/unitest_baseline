"""
QUESTION:
Implement a function `caesar_cipher` that employs the Caesar Cipher technique to decrypt a given encrypted text. The function should have one argument `txt` representing the encrypted text, and it should apply a fixed shift value of 3 to decrypt the text. The function should handle both uppercase and lowercase characters.
"""

def caesar_cipher(txt):
    """
    This function decrypts a given encrypted text using the Caesar Cipher technique with a fixed shift value of 3.
    
    Parameters:
    txt (str): The encrypted text to be decrypted.
    
    Returns:
    str: The decrypted text.
    """
    
    result = ""
    shift = 3
    
    # Apply the decryption shift value as 26 - shift
    decryption_shift = 26 - shift
    
    # Going through the encrypted text
    for char in txt:
        # Decrypting uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        
        # Decrypting lowercase characters
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    
    return result