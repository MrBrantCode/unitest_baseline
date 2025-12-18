"""
QUESTION:
Write a function named `difference_string` that takes two strings `s1` and `s2` as input. The function should return a new string containing characters present only in `s1` and not in `s2`. Ensure the function treats upper case and lower case characters separately, meaning 'a' and 'A' should be considered different characters.
"""

def difference_string(s1, s2):
    return_char = [ch for ch in s1 if ch not in s2]
    return "".join(return_char)