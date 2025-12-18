"""
QUESTION:
Create a function `check_chars(s, index, count_dict)` that takes a string `s`, an integer `index`, and a dictionary `count_dict` as parameters. The function should recursively iterate through the string, categorize each character as a vowel, consonant, numeric, space, or special character, and update the corresponding counts in `count_dict`. The function should be case-insensitive and handle alphabetic and numeric characters. The function should return the updated `count_dict`.
"""

def check_chars(s, index, count_dict):
    vowels = set("aeiou")
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    if index == len(s):
        return count_dict
    char = s[index].lower()
    if char in vowels:
        count_dict['vowels'] += 1
    elif char in alphabet:
        count_dict['consonants'] += 1
    elif char.isdigit():
        count_dict['numeric'] += 1
    elif char.isspace():
        count_dict['space'] += 1
    else:
        count_dict['special'] += 1
    return check_chars(s, index+1, count_dict)