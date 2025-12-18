"""
QUESTION:
Create a function `convert_to_dict` that takes a list of strings as input and returns a dictionary. The dictionary should have numbers as keys, starting from 1 and incrementing by 1 for each item, and strings in uppercase as values. The function should filter the input list to only include strings that have at least 5 characters, contain at least two vowels (A, E, I, O, U), and have no repeated characters.
"""

def convert_to_dict(lst):
    vowels = "AEIOU"
    result = {}
    count = 1
    
    for string in lst:
        uppercase_string = string.upper()
        
        if len(uppercase_string) >= 5 and len(set(uppercase_string)) == len(uppercase_string):
            vowel_count = 0
            for char in uppercase_string:
                if char in vowels:
                    vowel_count += 1
            if vowel_count >= 2:
                result[count] = uppercase_string
                count += 1
    
    return result