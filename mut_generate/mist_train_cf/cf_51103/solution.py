"""
QUESTION:
Create a function `remove_characters(s, t)` that takes two strings `s` and `t` as input and returns a new string where all occurrences of any character in `t` that are present in `s` are removed. The function should handle extended ASCII characters, special characters, and whitespaces in both strings.
"""

def remove_characters(s, t):
    t_set = set(t)  
    result = [char for char in s if char not in t_set]  
    return ''.join(result) 