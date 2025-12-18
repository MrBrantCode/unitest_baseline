"""
QUESTION:
Create a function named `count_upper_case_letters` that takes a string as input and returns the number of upper case letters in it. The function should not use any built-in string methods or functions that directly check for upper case letters. The function should handle edge cases such as empty strings, strings with no upper case letters, and strings that contain special characters or numbers, and have a time complexity of O(n), where n is the length of the input string.
"""

def count_upper_case_letters(string):
    if len(string) == 0:
        return 0
    return sum(1 for char in string if ord(char) >= 65 and ord(char) <= 90)