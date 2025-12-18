"""
QUESTION:
Create a function called `getValidStringLengths` that takes an array of strings as input and returns an array of integers representing the lengths of the valid strings. A valid string is one that is between 7 and 20 characters long (inclusive), contains only letters, and does not start with a vowel. If no valid strings are found, return an empty array.
"""

def getValidStringLengths(arr):
    valid_lengths = []
    
    for string in arr:
        if len(string) < 7 or len(string) > 20:
            continue
        
        if any(char.isdigit() or not char.isalpha() for char in string):
            continue
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        if string[0].lower() in vowels:
            continue
        
        valid_lengths.append(len(string))
    
    return valid_lengths