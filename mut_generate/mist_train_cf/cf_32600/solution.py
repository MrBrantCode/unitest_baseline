"""
QUESTION:
Implement a Python function `to_private_key(mnemonic: str) -> str` that takes a mnemonic phrase as input and returns the corresponding private key as a hexadecimal string, adhering to the BIP39 standard for mnemonic phrase to private key conversion. The function should handle the conversion of the mnemonic phrase to a private key in a secure and efficient manner.
"""

import hashlib
import binascii

def to_private_key(mnemonic: str) -> str:
    mnemonic_bytes = mnemonic.encode('utf-8')
    salt = b'mnemonic' + mnemonic_bytes
    seed = hashlib.pbkdf2_hmac('sha512', mnemonic_bytes, salt, 2048)
    private_key = seed[:32]  # First 32 bytes of the seed form the private key
    return binascii.hexlify(private_key).decode('utf-8')