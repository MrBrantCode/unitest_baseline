"""
QUESTION:
Write a function `last_index_of_substring` that finds the last index of a given substring within a string. The function should be case-sensitive, only consider substrings with a minimum length of 2 characters, and return the index of the last occurrence if there are multiple. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def last_index_of_substring(string, substring):
    if len(substring) < 2:
        return -1
    
    substring_len = len(substring)
    last_index = -1
    
    for i in range(len(string) - substring_len + 1):
        if string[i:i+substring_len] == substring:
            last_index = i
    
    return last_index