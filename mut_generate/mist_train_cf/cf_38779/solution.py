"""
QUESTION:
Implement a function `decrypt_message(socket_message: str, shift: int) -> str` that takes in an encrypted message `socket_message` and a shift value `shift`, and returns the decrypted message. The message is encrypted using a substitution cipher where each letter is replaced by another letter a fixed number of positions down the alphabet, wrapping around if necessary. Assume the input message contains only lowercase letters and spaces.
"""

def entrance(socket_message: str, shift: int) -> str:
    decrypted_message = ""
    for char in socket_message:
        if char == ' ':
            decrypted_message += ' '
        else:
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_message += shifted_char
    return decrypted_message