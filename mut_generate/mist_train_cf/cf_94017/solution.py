"""
QUESTION:
Write a function called `are_strings_equal` that takes two string parameters and returns a boolean value indicating whether the strings have the same content, ignoring any leading or trailing white spaces and special characters or punctuation marks. The function should have a time complexity of O(n), where n is the length of the longer string.
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