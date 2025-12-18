"""
QUESTION:
Design a function `string_to_emoji` that takes a string input and returns a string where each character is replaced with a corresponding emoji. The function should use a dictionary with 30 distinct emojis, including at least 10 numerical and 10 punctuation marks. The function should also be case-insensitive.
"""

emoji_code = {
    "0": "Emoji_1",
    "1": "Emoji_2",
    "2": "Emoji_3",
    "3": "Emoji_4",
    "4": "Emoji_5",
    "5": "Emoji_6",
    "6": "Emoji_7",
    "7": "Emoji_8",
    "8": "Emoji_9",
    "9": "Emoji_10",
    ".": "Emoji_11",
    ",": "Emoji_12",
    "!": "Emoji_13",
    "?": "Emoji_14",
    ":": "Emoji_15",
    ";": "Emoji_16",
    "-": "Emoji_17",
    "=": "Emoji_18",
    "+": "Emoji_19",
    "/": "Emoji_20",
    "A": "Emoji_21",
    "B": "Emoji_22",
    "C": "Emoji_23",
    "D": "Emoji_24",
    "E": "Emoji_25",
    "&": "Emoji_26",
    "*": "Emoji_27",
    "#": "Emoji_28",
    "@": "Emoji_29",
    "%": "Emoji_30"
}

def string_to_emoji(string):
    encoded_string = ""
    for char in string:
        if char.upper() in emoji_code:  # Making it case-insensitive
            encoded_string += emoji_code[char.upper()] + " "  # Space needed to differentiate consecutive emojis
    return encoded_string.rstrip()  # Remove possible trailing space