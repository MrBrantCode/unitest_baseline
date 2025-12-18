"""
QUESTION:
Create a function named `shared_chars` that takes two strings as input and returns a list of distinct characters that are common to both strings, ignoring case and handling Unicode characters. The returned list should be in alphabetical order.
"""

def shared_chars(s1, s2):
    set_s1 = set(s1.lower()) 
    set_s2 = set(s2.lower())
    
    shared = sorted(list(set_s1 & set_s2))
    return shared