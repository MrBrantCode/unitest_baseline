"""
QUESTION:
Create a function `check_unique_lowercase` that takes a string as an argument and returns `True` if all characters in the string are unique and lowercase alphabets only, and `False` otherwise. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def check_unique_lowercase(s):
    if len(s) > 26:
        return False
    alphabet_set = set()
    for char in s:
        if not char.islower():
            return False
        if char in alphabet_set:
            return False
        alphabet_set.add(char)
    return True