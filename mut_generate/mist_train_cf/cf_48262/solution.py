"""
QUESTION:
Design a function `xor_cipher` that implements a multi-layer XOR cipher to encode a textual communication using the key 'ABCDEFG'. The function should convert the key to its equivalent ASCII values and then perform the XOR operation on each character of the text with each character of the key in turn, rotating through the key characters as necessary. The function should not have any length restrictions on the text that can be encrypted.
"""

def xor_cipher(text):
    key = 'ABCDEFG'
    key_ord = [ord(k) for k in key]
    encrypted_text = ''
    
    for i in range(len(text)):
        # XOR operation with each character of the key in turn
        encrypted_char = chr(ord(text[i]) ^ key_ord[i % len(key_ord)])
        encrypted_text += encrypted_char
    
    return encrypted_text