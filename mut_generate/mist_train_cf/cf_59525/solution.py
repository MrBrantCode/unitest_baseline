"""
QUESTION:
Develop a function `translateToBraille(eng_string)` that takes a string of English letters (a-z or A-Z) and spaces as input and returns the Braille translation of the input string as a string of binary digits. The function should convert the input string to lowercase before translation and use a predefined Braille dictionary for translation. The Braille dictionary is a mapping of English letters and spaces to their corresponding Braille codes, which are 6-digit binary strings.
"""

# Braille dictionary
braille_dict = {
    "a": "100000",
    "b": "101000",
    "c": "110000",
    "d": "110100",
    "e": "100100",
    "f": "111000",
    "g": "111100",
    "h": "101100",
    "i": "011000",
    "j": "011100",
    "k": "100010",
    "l": "101010",
    "m": "110010",
    "n": "110110",
    "o": "100110",
    "p": "111010",
    "q": "111110",
    "r": "101110",
    "s": "011010",
    "t": "011110",
    "u": "100011",
    "v": "101011",
    "w": "011101",
    "x": "110011",
    "y": "110111",
    "z": "100111",
    " ": "000000"
}

def translate_to_braille(eng_string):
    return ''.join(braille_dict[char] for char in eng_string.lower())