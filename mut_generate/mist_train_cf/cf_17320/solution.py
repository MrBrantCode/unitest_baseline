"""
QUESTION:
Implement a function called `find_common_letters` that takes two strings as input and returns a dictionary where the keys are the common letters between the two strings and the values are the frequencies of each letter. The function should be case-insensitive and ignore non-alphabetic characters. Do not use any built-in Python functions or libraries for string manipulation or counting.
"""

def find_common_letters(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    common_letters = {}

    for char in str1:
        if char.isalpha() and char in str2:
            if char in common_letters:
                common_letters[char] += 1
            else:
                common_letters[char] = 1

    for char in str2:
        if char.isalpha() and char in str1:
            if char in common_letters:
                common_letters[char] += 1
            else:
                common_letters[char] = 1

    return common_letters