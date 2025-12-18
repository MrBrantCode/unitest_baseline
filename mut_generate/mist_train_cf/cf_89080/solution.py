"""
QUESTION:
Write a function named `contains_only_vowels` that takes a string as input and returns True if all characters in the string are vowels and False otherwise. The function should be case-insensitive, have a time complexity less than O(n log n), and a space complexity of O(1). The function should be able to handle strings with lengths up to 10^6 characters.
"""

def contains_only_vowels(s):
    vowels = set('aeiou')
    
    for char in s:
        if char.lower() not in vowels:
            return False
    
    return True