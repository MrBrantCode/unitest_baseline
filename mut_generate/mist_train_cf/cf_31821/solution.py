"""
QUESTION:
Implement a `decrypt_text` function that takes an encrypted text string as input and returns the decrypted text by reversing the characters of the input string. The function should handle both uppercase and lowercase letters, special characters, and spaces.
"""

def decrypt_text(encrypted_text):
    """
    This function decrypts the input encrypted text by reversing its characters.
    
    Parameters:
    encrypted_text (str): The input encrypted text string.
    
    Returns:
    str: The decrypted text string.
    """
    decrypted_text = encrypted_text[::-1]  # Reverse the characters of the encrypted text
    return decrypted_text