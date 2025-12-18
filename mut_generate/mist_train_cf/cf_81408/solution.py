"""
QUESTION:
Create a function called `replace_digits_with_words` that takes a string `s` as input and returns a new string where all numerical digits are replaced with their corresponding verbal annotations (e.g. "3" becomes "three", "4" becomes "four", etc.).
"""

def replace_digits_with_words(s):
    digits_to_words = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    result = ""
    for char in s:
        if char.isdigit():
            result += digits_to_words[char]
        else:
            result += char
    return result