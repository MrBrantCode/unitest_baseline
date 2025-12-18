"""
QUESTION:
Write a function `last_index_of_substring(string, substring)` that finds the last index of a given case-sensitive substring in a string. The function should only consider substrings with a length of at least two characters and should only be used with input strings that contain at least one occurrence of the substring. If multiple occurrences exist, it should return the index of the last occurrence. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
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