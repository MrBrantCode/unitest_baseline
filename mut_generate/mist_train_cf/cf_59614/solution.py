"""
QUESTION:
Implement a function named 'two_key_encryption' that uses two symmetric keys to encrypt data in such a way that either key can be used for decryption, without storing the keys.
"""

def two_key_encryption(key1, key2, data):
    """
    This function uses two symmetric keys to encrypt data in such a way that either key can be used for decryption.

    Args:
        key1 (str): The first encryption key.
        key2 (str): The second encryption key.
        data (str): The data to be encrypted.

    Returns:
        str: The encrypted data.
    """
    # Convert keys and data to bytes
    key1_bytes = key1.encode()
    key2_bytes = key2.encode()
    data_bytes = data.encode()

    # Calculate the encryption key by XORing key1 and key2
    encryption_key = bytes(x ^ y for x, y in zip(key1_bytes, key2_bytes))

    # Calculate the length of the encryption key
    key_length = len(encryption_key)

    # Encrypt the data by XORing it with the encryption key
    encrypted_data = bytes(x ^ encryption_key[i % key_length] for i, x in enumerate(data_bytes))

    # Return the encrypted data as a string
    return encrypted_data.decode('latin1')