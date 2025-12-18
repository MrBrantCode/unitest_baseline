"""
QUESTION:
Given two strings `s` and `t`, write a function `isAnagram` to return `true` if `t` is an anagram of any permutation of the string `s`. The function should take two parameters `s` and `t` of type `str` and return a `bool` value. Both `s` and `t` consist of only lowercase English letters and have lengths between 1 and 5000 inclusive.
"""

def isAnagram(s: str, t: str) -> bool:
    """
    Checks if string `t` is an anagram of any permutation of the string `s`.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if `t` is an anagram of `s`, False otherwise.
    """
    
    # If the lengths of both strings are not equal, then they can not be an anagrams.
    if len(s) != len(t):
        return False
    
    # Create a dictionary for each string
    dic_s = {}
    dic_t = {}

    for c in s:
        if c in dic_s:
            dic_s[c] += 1
        else:
            dic_s[c] = 1
            
    for c in t:
        if c in dic_t:
            dic_t[c] += 1
        else:
            dic_t[c] = 1
            
    # If both dictionaries are the same, the strings are anagram of each other
    if dic_s == dic_t:
        return True
    
    return False