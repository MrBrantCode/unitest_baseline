"""
QUESTION:
Write a function `find_longest_string` that finds the length of the longest string between two given substrings in a string, where the starting substring is immediately followed by the ending substring. The function should be case-insensitive and consider special characters, numbers, and whitespace. If either substring is not found, it should return 0.
"""

def find_longest_string(string, start_substring, end_substring):
    start_substring = start_substring.lower()
    end_substring = end_substring.lower()
    start_index = string.lower().find(start_substring)
    end_index = string.lower().find(end_substring)
    if start_index == -1 or end_index == -1:
        return 0
    substring_between = string[start_index+len(start_substring):end_index].strip()
    return len(substring_between)