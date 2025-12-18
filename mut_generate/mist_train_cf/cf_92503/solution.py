"""
QUESTION:
Create a function `contains_only_vowels` that takes a string as input and returns `True` if the string contains only vowels and `False` otherwise. The function should have a time complexity of less than O(n^2), where n is the length of the input string.
"""

def contains_only_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char.lower() not in vowels:
            return False
    return True