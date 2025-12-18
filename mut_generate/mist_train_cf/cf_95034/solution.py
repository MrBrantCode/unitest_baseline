"""
QUESTION:
Write a function `search_substrings` that takes a string and a list of substrings as input. The function should return a dictionary where the keys are the substrings and the values are the number of times each substring appears in the string. The function should ignore case, only consider alphanumeric characters, and handle non-contiguous and varying length substrings.
"""

import re

def search_substrings(string, substrings):
    # Ignore case
    string = string.lower()
    substrings = [substring.lower() for substring in substrings]
    
    # Consider only alphanumeric characters
    string = re.sub(r'[^a-zA-Z0-9]', '', string)
    substrings = [re.sub(r'[^a-zA-Z0-9]', '', substring) for substring in substrings]
    
    # Initialize count dictionary
    count_dict = {substring: 0 for substring in substrings}
    
    # Search for substrings
    for substring in substrings:
        i = 0
        while i < len(string):
            index = string.find(substring, i)
            if index == -1:
                break
            count_dict[substring] += 1
            i = index + len(substring)
    
    return count_dict