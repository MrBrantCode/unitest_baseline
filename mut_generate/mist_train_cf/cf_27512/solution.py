"""
QUESTION:
Implement the `encrypt` and `decrypt` methods of the `SimpleEncryption` class.

In the `encrypt` method, take a message as input and return the encrypted message using the partner's key. The partner's key is set using the `setPartner` method, which is called before the `encrypt` method. Each character of the message should be encrypted by adding the partner's key modulo 256 and then converting the result back to a character.

In the `decrypt` method, take an encrypted message as input and return the decrypted message using the partner's key. Each character of the encrypted message should be decrypted by subtracting the partner's key modulo 256 and then converting the result back to a character. The partner's key is the same as the one used for encryption.
"""

def encrypt(message, key):
    """
    Encrypts a message using the partner's key.

    Args:
    message (str): The message to be encrypted.
    key (int): The partner's key.

    Returns:
    str: The encrypted message.
    """
    encryptedMessage = ""
    for character in message:
        encryptedChar = chr((ord(character) + key) % 256)
        encryptedMessage += encryptedChar
    return encryptedMessage

def decrypt(encryptedMessage, key):
    """
    Decrypts an encrypted message using the partner's key.

    Args:
    encryptedMessage (str): The encrypted message.
    key (int): The partner's key.

    Returns:
    str: The decrypted message.
    """
    decryptedMessage = ""
    for character in encryptedMessage:
        decryptedChar = chr((ord(character) - key) % 256)
        decryptedMessage += decryptedChar
    return decryptedMessage