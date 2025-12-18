"""
QUESTION:
Write a function `search_substrings` that takes two parameters: `string` and `substrings`, where `string` is the main string to search in and `substrings` is a list of substrings to search for. The function should return a dictionary where the keys are the substrings and the values are the counts of occurrences of each substring in the string.

The function should ignore case, consider only alphanumeric characters, handle non-contiguous and varying length substrings, and return counts for each substring. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(m), where m is the total number of characters in all the substrings.
"""

import re

def search_substrings(string, substrings):
    """
    Searches for occurrences of a list of substrings in a given string.

    Args:
        string (str): The main string to search in.
        substrings (list): A list of substrings to search for.

    Returns:
        dict: A dictionary where keys are the substrings and values are their counts.

    """
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