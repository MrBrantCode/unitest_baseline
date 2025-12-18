"""
QUESTION:
Create a function named `is_anagram` that takes two string parameters, `str1` and `str2`, and returns `True` if the strings are anagrams of each other (ignoring case and spaces), and `False` otherwise. The function should be case-insensitive and disregard any spaces in the strings.
"""

def is_anagram(str1, str2):
    str1 = str1.replace(' ', '').lower()  # Remove spaces and convert to lowercase
    str2 = str2.replace(' ', '').lower()  # Remove spaces and convert to lowercase

    if len(str1) != len(str2):  # Strings of different length cannot be anagrams
        return False

    count = {}  # A dictionary to count character frequency

    # Analyzing characters in str1
    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Evaluating frequency and distribution in str2
    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            return False

    # Checking that each character count is 0
    for k in count:
        if count[k] != 0:
            return False

    return True