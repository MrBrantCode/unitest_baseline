"""
QUESTION:
Design a Python function `mergedAlphabets` that takes two string parameters. The function should return a new string that contains all alphabetic characters from both input strings, removing any non-alphabetic characters and duplicates, and sorting the characters in ascending order.
"""

def mergedAlphabets(string1, string2):
    # concatinate the strings
    merged_string = string1 + string2
    # remove non-alphabetic characters
    alphabetic_merged_string = ''.join(ch for ch in merged_string if ch.isalpha())
    # remove duplicates and sort
    unique_sorted_string = ''.join(sorted(set(alphabetic_merged_string)))
    return unique_sorted_string