"""
QUESTION:
Implement a function named `xor_cipher` that takes two parameters: `input_string` and `key`, both of which are strings. The function should use the XOR cipher methodology to encrypt or decrypt the input string using the provided key, handling multibyte characters properly by repeating the key if necessary. The function should return the encrypted or decrypted string.
"""

def xor_cipher(input_string, key):
    """
    This function implements XOR cipher methodology to encrypt/decrypt input string.
    
    Parameters:
    input_string: A string that you want to encrypt/decrypt.
    key : A secret key as a string used for encryption and decryption

    Returns:
    An encrypted/decrypted string based on input_string
    """

    # Convert input string into bytes array
    input_bytes = input_string.encode('utf-8')
    
    # Convert key into bytes
    key_bytes = key.encode('utf-8')
    key_length = len(key_bytes)

    # A list to hold xor result
    xor_result = bytearray()

    # Apply XOR operation
    for i in range(len(input_bytes)):
        xor_result.append(input_bytes[i] ^ key_bytes[i % key_length])

    # Convert result into string and return
    return xor_result.decode('utf-8')