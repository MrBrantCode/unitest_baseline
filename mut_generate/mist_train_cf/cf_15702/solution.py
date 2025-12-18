"""
QUESTION:
Implement a function `convert_string(input_string)` that converts a given string with no spaces to a string with underscores (_) in all spaces between words. The input string will consist only of uppercase and lowercase letters and may contain punctuation marks. The output string should have all words separated by a single underscore, and all punctuation marks should be removed. The function should handle cases where multiple consecutive spaces occur between words and should replace them with a single underscore, ignore non-alphabet characters, and remove leading and trailing spaces. The function should have a time complexity of O(n), where n is the length of the input string, and avoid using unnecessary memory space.
"""

import string

def convert_string(input_string):
    input_string = input_string.strip()
    words = []
    current_word = ""

    for char in input_string:
        if char.isalpha():
            current_word += char
        elif char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        elif char in string.punctuation:
            continue

    if current_word:
        words.append(current_word)

    return "_".join(words)