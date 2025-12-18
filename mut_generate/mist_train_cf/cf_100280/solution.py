"""
QUESTION:
Write a function named `remove_common_characters` that takes two strings `s` and `t` as input and returns two new strings with all common characters removed. The function should not use any external libraries and should be efficient enough to handle strings of up to 1000 characters.
"""

def remove_common_characters(s, t):
    """
    This function takes two strings `s` and `t` as input and returns two new strings with all common characters removed.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    tuple: A tuple of two strings with common characters removed.
    """
    common = set()
    for i in range(len(s)):
        if s[i] in t:
            common.add(s[i])
    for c in common:
        s = s.replace(c, '')
        t = t.replace(c, '')
    return s, t