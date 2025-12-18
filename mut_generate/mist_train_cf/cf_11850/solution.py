"""
QUESTION:
Write a function `arePermutations(string1, string2)` that determines whether two input strings are permutations of each other, considering case sensitivity and ignoring spaces and punctuation marks. The function should have a time complexity of O(n log n).
"""

import re

def arePermutations(string1, string2):
    """
    Determine whether two input strings are permutations of each other, 
    considering case sensitivity and ignoring spaces and punctuation marks.

    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.

    Returns:
        bool: True if the input strings are permutations of each other, False otherwise.
    """

    # Remove spaces and punctuation marks
    string1 = re.sub('[^a-zA-Z0-9]', '', string1)
    string2 = re.sub('[^a-zA-Z0-9]', '', string2)

    # Convert to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Check lengths
    if len(string1) != len(string2):
        return False

    # Sort strings
    sortedString1 = sorted(string1)
    sortedString2 = sorted(string2)

    # Compare sorted strings
    return sortedString1 == sortedString2