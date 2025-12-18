"""
QUESTION:
Write a function called `are_strings_equal` that takes two strings as input, removes leading and trailing white spaces, removes special characters and punctuation marks, and checks if the modified strings are equal. The time complexity should be O(n), where n is the length of the longer string.
"""

def are_strings_equal(str1, str2):
    # Remove leading and trailing white spaces
    str1 = str1.strip()
    str2 = str2.strip()

    # Remove special characters and punctuation marks
    special_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in special_chars:
        str1 = str1.replace(char, '')
        str2 = str2.replace(char, '')

    # Check if the modified strings are equal
    return str1 == str2