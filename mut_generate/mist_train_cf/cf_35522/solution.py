"""
QUESTION:
Create a function named `count_substring_occurrences` that takes in a list of strings and a regular expression pattern. The function should return a dictionary where the keys are the matched substrings from the regular expression pattern, and the values are the counts of occurrences of each substring within the list of strings. The function should handle any valid regular expression pattern and any list of strings.
"""

import re

def count_substring_occurrences(string_list, pattern):
    substring_counts = {}
    regex = re.compile(pattern)
    
    for string in string_list:
        matches = regex.finditer(string)
        for match in matches:
            matched_substring = match.group()
            if matched_substring in substring_counts:
                substring_counts[matched_substring] += 1
            else:
                substring_counts[matched_substring] = 1
    
    return substring_counts