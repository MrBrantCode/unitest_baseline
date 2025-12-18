"""
QUESTION:
Write a function `convert_to_dict` that takes a list of strings as input and returns a dictionary. The dictionary's keys should be ascending integers starting from 1, and its values should be the input strings converted to uppercase. Include only strings that have at least 5 characters, contain at least two vowels (A, E, I, O, U), and have no repeated characters.
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