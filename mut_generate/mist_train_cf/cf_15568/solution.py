"""
QUESTION:
Write a function `get_strings_with_ct` that takes a list of strings as input and returns a list of strings where each string starts with 'c' and ends with 't'. The function should have a time complexity of O(n), where n is the total number of characters in all the strings combined, and a space complexity of O(m), where m is the number of strings in the list that satisfy the condition.
"""

def get_strings_with_ct(list_strings):
    result = []
    for string in list_strings:
        if string[0] == 'c' and string[-1] == 't':
            result.append(string)
    return result