"""
QUESTION:
Write a function named `get_strings_with_ct` that takes a list of strings as input. The function should return a list of strings where each string's first character is 'c' and last character is 't'. The function should have a time complexity of O(n), where n is the total number of characters in all the strings combined, and a space complexity of O(m), where m is the number of strings in the list that satisfy the condition.
"""

def get_strings_with_ct(list_strings):
    return [string for string in list_strings if string and string[0] == 'c' and string[-1] == 't']