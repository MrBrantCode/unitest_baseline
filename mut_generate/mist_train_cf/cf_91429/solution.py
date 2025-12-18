"""
QUESTION:
Write a function called `find_common_letters` that takes two strings as input. The function should return a dictionary containing the common letters between the two strings, with each key being a common letter and its corresponding value representing the maximum frequency of that letter in either string. The function should be case-insensitive and ignore non-alphabet characters.
"""

def find_common_letters(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    common_letters = {}
    for letter in string1:
        if letter.isalpha() and letter in string2:
            if letter in common_letters:
                common_letters[letter] = max(common_letters[letter], string2.count(letter))
            else:
                common_letters[letter] = string2.count(letter)
    return common_letters