"""
QUESTION:
Given a string `s`, write a function named `distinct_substrings` that returns a dictionary where the keys are the distinct substrings of `s` and the values are their respective counts.

Constraints: `1 <= s.length <= 500` and `s` consists of lowercase English letters. Follow up: Can you solve this problem in `O(n)` time complexity?
"""

def distinct_substrings(s):
    """
    This function generates all substrings of a given string and returns a dictionary 
    where the keys are the distinct substrings and the values are their respective counts.

    Args:
    s (str): The input string.

    Returns:
    dict: A dictionary where the keys are the distinct substrings of `s` and the values are their respective counts.
    """
    n = len(s)
    substrings = dict()
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if sub in substrings:
                substrings[sub] += 1
            else:
                substrings[sub] = 1
    return substrings