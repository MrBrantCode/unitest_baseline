"""
QUESTION:
Create a function `create_char_occurrences_dict` that takes a string as input and returns a dictionary where keys are characters and values are the occurrences of that character in the string, excluding any characters that are vowels and any characters that are repeated consecutively in the string, with a time complexity of less than O(n^2). The occurrences should be case-sensitive.
"""

def create_char_occurrences_dict(string):
    char_dict = {}
    i = 0
    
    while i < len(string):
        char = string[i]
        
        # Check if character is a vowel
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            i += 1
            continue
        
        # Check if character is repeated consecutively
        if i < len(string) - 1 and string[i+1] == char:
            i += 1
            continue
        
        # Update character occurrences dictionary
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
        
        i += 1
    
    return char_dict