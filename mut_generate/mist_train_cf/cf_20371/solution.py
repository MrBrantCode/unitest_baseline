"""
QUESTION:
Create a function called `contains_only_vowels` that takes a string as input and returns a boolean indicating whether the string contains only vowels. The vowels are 'a', 'e', 'i', 'o', and 'u', and the check should be case-insensitive. The function should have a time complexity less than O(n log n) and a space complexity of O(1).
"""

def contains_only_vowels(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    
    for char in s:
        if char.lower() not in vowels:
            return False
    
    return True