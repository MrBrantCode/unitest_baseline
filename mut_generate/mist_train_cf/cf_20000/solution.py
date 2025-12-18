"""
QUESTION:
Create a function `count_upper_case_letters` that takes a string as input and returns the number of upper case letters in the string. The function must not use any built-in string methods or functions that directly check for upper case letters. The solution should have a time complexity of O(n), where n is the length of the input string.
"""

def count_upper_case_letters(string):
    count = 0
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            count += 1
    return count