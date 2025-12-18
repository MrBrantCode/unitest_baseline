"""
QUESTION:
Write a function `search_substrings(string, substrings)` that searches for multiple substrings in a string, ignoring case and non-alphanumeric characters. The function should return a dictionary with the count of occurrences for each substring found in the string. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(m), where m is the total number of characters in all the substrings.
"""

import re

def search_substrings(string, substrings):
    # Ignore case of the string and substrings
    string = string.lower()
    substrings = [substring.lower() for substring in substrings]

    # Keep only alphanumeric characters in the string and substrings
    string = re.sub(r'[^a-zA-Z0-9]', '', string)
    substrings = [re.sub(r'[^a-zA-Z0-9]', '', substring) for substring in substrings]

    # Count the occurrences of each substring in the string
    occurrences = {substring: 0 for substring in substrings}
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            sub = string[i:j]
            if sub in occurrences:
                occurrences[sub] += 1

    return occurrences