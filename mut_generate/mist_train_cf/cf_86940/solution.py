"""
QUESTION:
Write a function `check_string` that takes a string as input and returns `True` if the string consists only of lowercase alphabetic characters and contains at least one vowel, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def check_string(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Check if the string is empty
    if not string:
        return False
    
    # Check if all characters are lowercase alphabets and contains at least one vowel
    has_vowel = False
    for char in string:
        if not char.islower() or char in vowels:
            if char in vowels:
                has_vowel = True
            if not char.islower():
                return False
    return has_vowel