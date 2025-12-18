"""
QUESTION:
Implement a function `decrypt_message(encrypted_text: str) -> str` that takes a string `encrypted_text` containing uppercase letters, lowercase letters, and spaces, encrypted using the ROT13 substitution cipher, and returns the decrypted message while retaining the original letter case and spaces.
"""

def decrypt_message(encrypted_text: str) -> str:
    decrypted = ""
    for symbol in encrypted_text:
        if symbol.isalpha():
            if symbol.islower():
                decrypted += chr(((ord(symbol) - ord('a') - 13) % 26) + ord('a')) if symbol >= 'n' else chr(((ord(symbol) - ord('a') + 13) % 26) + ord('a'))
            else:
                decrypted += chr(((ord(symbol) - ord('A') - 13) % 26) + ord('A')) if symbol >= 'N' else chr(((ord(symbol) - ord('A') + 13) % 26) + ord('A'))
        else:
            decrypted += symbol
    return decrypted