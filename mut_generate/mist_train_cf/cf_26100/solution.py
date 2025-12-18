"""
QUESTION:
Write a function `findPattern` that takes two strings, `str1` and `str2`, and returns 1 if `str2` is a subsequence of `str1`, and 0 otherwise. The function should check if all characters in `str2` appear in the same order in `str1`.
"""

def findPattern(str1, str2):
    """
    Checks if str2 is a subsequence of str1.
    
    Args:
        str1 (str): The main string.
        str2 (str): The string to be checked as a subsequence.
    
    Returns:
        int: 1 if str2 is a subsequence of str1, 0 otherwise.
    """

    ind = 0
    for ch in str2: 
        if ch not in str1[ind:]: 
            return 0
  
        ind = str1.index(ch, ind) + 1
 
    return 1