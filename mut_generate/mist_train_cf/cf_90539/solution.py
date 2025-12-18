"""
QUESTION:
Write a function `check_strings(arr)` that checks if all strings in a given sequence `arr` meet the following conditions: the string length is between 3 and 10 characters, the string contains only lowercase alphabets, the string has at least one vowel, and all strings in the sequence are unique.
"""

def check_strings(arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    seen = set()
    
    for string in arr:
        # Check if string length is between 3 and 10 characters
        if len(string) < 3 or len(string) > 10:
            return False
        
        # Check if string contains only lowercase alphabets
        if not string.islower() or not string.isalpha():
            return False
        
        # Check if string contains at least one vowel
        if not any(vowel in string for vowel in vowels):
            return False
        
        # Check if string is unique
        if string in seen:
            return False
        seen.add(string)
    
    return True