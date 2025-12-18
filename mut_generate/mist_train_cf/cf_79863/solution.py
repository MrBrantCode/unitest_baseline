"""
QUESTION:
Implement a function called `encrypt` and `decrypt` that encrypts and decrypts a given string of characters, including special characters and numbers, using a provided key. The encryption should be reversible, allowing the original string to be recovered after decryption. The key should be used for both encryption and decryption, and the functions should support ASCII characters with codes between 32 and 127. The functions should return the encrypted and decrypted strings, respectively.
"""

def encrypt(text, key):
    """Encrypts a given string of characters using a provided key."""
    key = list(key)
    chars = list(map(chr, range(32, 127))) 
    enc_chars = key+list(filter(lambda x: x not in key, chars)) 
    lookup_table = dict(zip(chars, enc_chars)) 
    cipher = "".join([lookup_table[c] for c in text])
    return cipher

def decrypt(cipher, key):
    """Decrypts a given string of characters using a provided key."""
    key = list(key)
    chars = list(map(chr, range(32, 127))) 
    enc_chars = key+list(filter(lambda x: x not in key, chars)) 
    lookup_table = dict(zip(enc_chars, chars)) 
    text = "".join([lookup_table[c] for c in cipher])
    return text