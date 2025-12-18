"""
QUESTION:
Write a function `contains_only_vowels` that takes a string as input and returns `True` if the string contains only vowels and `False` otherwise. The function should have a time complexity less than O(n log n) and a space complexity of O(1), and should be able to handle strings of up to 10^6 characters. The function should be case-insensitive, treating both lowercase and uppercase vowels as vowels.
"""

def contains_only_vowels(s):
    vowels = set('aeiou')
    
    for char in s:
        if char.lower() not in vowels:
            return False
    
    return True