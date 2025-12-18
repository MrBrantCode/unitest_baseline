"""
QUESTION:
Write a function `decode_message(encoded_message)` that takes a list of strings `encoded_message` as input and returns the decoded message. The message is encoded using a simple substitution cipher where each character is shifted to a different character. The function should reverse the substitution cipher to recover the original message. The substitution cipher is predefined and should be used to decode the message. The decoded message should be returned as a single string with each line separated by a newline character.
"""

def decode_message(encoded_message):
    cipher = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
        'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a', '8': ' ', '`': 'o', 'P': 'l', 'Y': 'W',
        ',': 'H', ' ': '!', '1': '0', '2': '9', '3': '8', '4': '7', '5': '6', '6': '5', '7': '4', '9': '2',
        '0': '1', '\"': 'I'
    }

    decoded_message = ""
    for line in encoded_message:
        decoded_line = ""
        for char in line:
            if char in cipher:
                decoded_line += cipher[char]
            else:
                decoded_line += char
        decoded_message += decoded_line + "\n"
    return decoded_message