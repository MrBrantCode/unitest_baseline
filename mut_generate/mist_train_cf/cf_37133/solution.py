"""
QUESTION:
Write a function `decode_emojis` that takes a list of emoji codes as input, where each code is a hexadecimal string. The function should return a string of the corresponding emoji characters. If a given emoji code is invalid (i.e., not a valid hexadecimal string), the function should skip that code and continue decoding the remaining codes.
"""

def decode_emojis(emoji_codes):
    decoded_emojis = []
    for emojicode in emoji_codes:
        try:
            emoji = chr(int(emojicode, 16))
            decoded_emojis.append(emoji)
        except ValueError:
            pass
    return ''.join(decoded_emojis)