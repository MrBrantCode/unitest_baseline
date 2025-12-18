"""
QUESTION:
Write a program that provides four functions: `string_to_hex(s)`, `hex_to_string(h)`, `encrypt(s, key)`, and `decrypt(encrypted, key)`. 

- The `string_to_hex(s)` function should take a string `s` and return its hexadecimal representation.
- The `hex_to_string(h)` function should take a hexadecimal string `h` and return the original string.
- The `encrypt(s, key)` function should take a string `s` and a key, convert the string to hexadecimal, encrypt the hexadecimal string using the key with XOR encryption, and return the encrypted hexadecimal string.
- The `decrypt(encrypted, key)` function should take an encrypted hexadecimal string and a key, decrypt the string using the key with XOR encryption, convert it back to hexadecimal, and return the original string.

The key can be any integer, and the functions should be able to handle edge cases without crashing.
"""

import codecs

def string_to_hex(s):
    return codecs.encode(s.encode(), "hex").decode()

def hex_to_string(h):
    return codecs.decode(h.encode(), "hex").decode()

def xor_with_key(s, key):
    return "".join(chr(ord(c) ^ key) for c in s)

def entrance(s, key, mode):
    if mode == 'encrypt':
        hex_str = string_to_hex(s)
        encrypted_str = xor_with_key(hex_str, key)
        return codecs.encode(encrypted_str.encode(), "hex").decode()
    elif mode == 'decrypt':
        encrypted_str = codecs.decode(s.encode(), "hex").decode()
        hex_str = xor_with_key(encrypted_str, key)
        return hex_to_string(hex_str)