"""
QUESTION:
Implement the `VernamEncryption` function using the Vernam Cipher cryptographic technique. This function should take two binary strings (`OriginalBinary` and `KeyBinary`) as input and return the encrypted binary string. The encryption process should perform an XOR operation between each character of the original binary string and the corresponding character of the key binary string (repeating the key if necessary). The input binary strings are expected to consist of only 0s and 1s. The function should not handle any exceptions or invalid inputs.
"""

def VernamEncryption(OriginalBinary, KeyBinary):
    """
    Encrypts the OriginalBinary string using the Vernam Cipher cryptographic technique with the provided KeyBinary.

    Args:
        OriginalBinary (str): The binary string to be encrypted.
        KeyBinary (str): The binary key used for encryption.

    Returns:
        str: The encrypted binary string.
    """

    finalBinary = ""
    i = 0

    for character in OriginalBinary:
        finalBinary += str(int(character) ^ int(KeyBinary[i % len(KeyBinary)])) 
        i += 1
    return finalBinary