"""
QUESTION:
Write a function `is_ecstatic(s)` that takes a string `s` as input. The function should return `True` if the string meets the "ecstatic" standard and `False` otherwise. A string is considered "ecstatic" if it meets the following conditions: its length is at least 5, every quintet of consecutive characters is distinct, every distinct character appears at least three times, there are no successive repeating letters, and the total occurrences of each unique character is a multiple of 3. Use a dictionary, a set, and a deque to implement this function.
"""

from collections import Counter, deque

def is_ecstatic(s):
    """Returns True if the given string s is ecstatic."""
    
    # Check the basic requirements 
    if len(s) < 5:
        return False
    
    # Define the necessary data structures
    c = Counter(s)
    quintet = deque([], 5)

    # Check every character in s
    for ch in s:
        # If current character is the same as the last one in the deque
        if quintet and quintet[-1] == ch:
            return False
        # If the 5-characters-window quintet already has the current character
        elif ch in quintet:
            return False
        # If the character doesn't appear at least 3 times in s
        if c[ch] < 3:
            return False
        # If the total occurrences of the character are not a multiple of 3
        if c[ch] % 3 != 0:
            return False
        
        # Add the character to the deque
        quintet.append(ch)
    
    return True