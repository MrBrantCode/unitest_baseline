"""
QUESTION:
Create a function called `encrypt_variable` that takes a string as input, encrypts it using a custom encryption algorithm where each character is shifted by 1 in ASCII value, then decrypts the encrypted string using the reverse operation, and finally returns the decrypted string. The function should include error handling to catch any decryption errors and raise an exception with the message "Error: Decryption failed."
"""

def encrypt_variable(value):
    try:
        encrypted_value = "".join(chr(ord(char) + 1) for char in value)
        decrypted_value = "".join(chr(ord(char) - 1) for char in encrypted_value)
        return decrypted_value
    except:
        raise Exception("Error: Decryption failed.")