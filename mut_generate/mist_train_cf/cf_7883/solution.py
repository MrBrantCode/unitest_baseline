"""
QUESTION:
Implement the function `find_substring(string, substring)` that outputs the index of the first occurrence of the substring in the string. The substring should match the entire word, not just a part of it, and the comparison should be case-insensitive. If the substring is not found in the string, return -1. The function should be able to handle strings and substrings of length up to 10^6 characters.
"""

def find_substring(string, substring):
    string = string.lower()
    substring = substring.lower()
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    
    return -1