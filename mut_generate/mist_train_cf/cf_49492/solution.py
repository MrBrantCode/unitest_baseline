"""
QUESTION:
Create a function `vigenere_cipher_encode` and a function `vigenere_cipher_decode` that implement the Vigenere cipher algorithm to encode and decode messages, respectively. The functions should handle both lowercase and uppercase letters, preserve case, and leave non-alphabet characters unchanged. The shift for each character in the message is determined by the corresponding character in the key, repeating the key as necessary.
"""

def vigenere_cipher_encode(text, key):
    """Encode a message with a Vigenere cipher"""
    result = ''
    
    key_index = 0
    for char in text:
        key_char = key[key_index % len(key)]
        
        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
        
        key_index += 1
        
    return result


def vigenere_cipher_decode(cipher, key):
    """Decode a Vigenere cipher back into the original message"""
    result = ''
    
    key_index = 0
    for char in cipher:
        key_char = key[key_index % len(key)]
        
        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
        
        key_index += 1
        
    return result