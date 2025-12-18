"""
QUESTION:
Design a function called `find_all_substrings(s)` that takes a string `s` as input and returns a list of all possible substrings of `s`. The function should include single-character substrings and the entire string itself, and its time complexity should be O(n^2), where n is the length of the string.
"""

def find_all_substrings(s):
    """
    This function generates all possible substrings of a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    list: A list of all possible substrings of the input string.
    """
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings