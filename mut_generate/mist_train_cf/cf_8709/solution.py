"""
QUESTION:
Write a function `check_strings` that takes a sequence of strings as input and returns `True` if all strings in the sequence meet the following conditions: 
- Each string contains only lowercase alphabets.
- The length of each string is between 3 and 10 characters (inclusive).
- Each string contains at least one vowel ('a', 'e', 'i', 'o', or 'u').
- All strings in the sequence are unique.
"""

def check_strings(arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    seen = set()
    
    for string in arr:
        # Check if string length is between 3 and 10 characters
        if len(string) < 3 or len(string) > 10:
            return False
        
        # Check if string contains only lowercase alphabets
        if not string.islower():
            return False
        
        # Check if string contains at least one vowel
        if not any(vowel in string for vowel in vowels):
            return False
        
        # Check if string is unique
        if string in seen:
            return False
        seen.add(string)
    
    return True