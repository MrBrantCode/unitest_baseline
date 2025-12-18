"""
QUESTION:
Write a function `convert_two_chars_uppercase` that takes a string `s` as input. The function should convert the last two characters of each word in the string to uppercase and return the resulting string. If a word has less than two characters, the entire word should be converted to uppercase.
"""

def convert_two_chars_uppercase(s):
    s = s.split()
    new_string = []
    for word in s:
        if len(word) < 2:
            new_word = word.upper()
        else:
            new_word = word[:-2] + word[-2:].upper()
        new_string.append(new_word)
    return ' '.join(new_string)