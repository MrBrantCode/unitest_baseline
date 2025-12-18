"""
QUESTION:
Write a function named `find_substring` that takes two parameters: `string` and `substring`. The function should return the index of the first occurrence of the `substring` in the `string`, where the `substring` matches the entire word and the search is case-insensitive. If the `substring` is not found in the `string`, the function should return -1. The function should be able to handle strings and substrings of up to 10^6 characters in length.
"""

def find_substring(string, substring):
    string = string.lower()
    substring = substring.lower()
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    
    return -1