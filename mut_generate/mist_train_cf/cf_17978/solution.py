"""
QUESTION:
Write a function `find_strings_with_substring` that takes a list of strings and a string, and returns a list containing all unique strings from the given list that have the given string as a substring. The search for substrings should be case-sensitive. The function should have a time complexity of O(n*m) and a space complexity of O(n), where n is the number of strings and m is the maximum number of characters in a string.
"""

def find_strings_with_substring(strings, substring):
    result = []
    for string in strings:
        if substring in string and string not in result:
            result.append(string)
    return result