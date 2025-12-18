"""
QUESTION:
Create a function `obfuscate_email` to encrypt an email address using a combination of ROT13 and Base64 encoding algorithms. The function should take an email address as input and return the encrypted email address as a string. The function should not have any dependencies on external libraries or databases.
"""

def obfuscate_email(email):
    """
    Encrypt an email address using a combination of ROT13 and Base64 encoding algorithms.

    Args:
    email (str): The email address to be encrypted.

    Returns:
    str: The encrypted email address.
    """
    # Implement the ROT13 encoding algorithm
    rot13_email = ''.join(chr((ord(char) - 97 + 13) % 26 + 97) if 'a' <= char <= 'z' 
                           else chr((ord(char) - 65 + 13) % 26 + 65) if 'A' <= char <= 'Z' 
                           else char for char in email)

    # Implement the Base64 encoding algorithm
    import base64
    base64_email = base64.b64encode(rot13_email.encode()).decode()

    return base64_email