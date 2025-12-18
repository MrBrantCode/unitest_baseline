"""
QUESTION:
Create a function `count_uppercase_letters` that takes two parameters: a string and an optional boolean parameter `case_insensitive` with a default value of `False`. The function should return the number of upper case letters in the string, or the total number of letters if `case_insensitive` is `True`. The function should not use built-in string methods or functions that directly check for upper case letters, and should have a time complexity of O(n), where n is the length of the input string. The function should correctly handle edge cases such as empty strings, strings with no upper case letters, and strings that contain special characters or numbers, and should work with strings that contain multiple languages and character encodings, such as UTF-8.
"""

def count_uppercase_letters(string, case_insensitive=False):
    count = 0
    for char in string:
        if ord('A') <= ord(char) <= ord('Z'):
            count += 1
        elif case_insensitive and ord('a') <= ord(char) <= ord('z'):
            count += 1
    return count