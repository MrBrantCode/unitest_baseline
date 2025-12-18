"""
QUESTION:
Write a function `count_vowels_and_consonants` that takes a string `my_str` as input. The function should return the number of unique vowels and consonants in the string, excluding duplicates and non-alphabetic characters. The function should be case-insensitive and consider 'a', 'e', 'i', 'o', 'u' as vowels and all other alphabets as consonants.
"""

def count_vowels_and_consonants(my_str):
    vowels = set()
    consonants = set()
    
    for char in my_str:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels.add(char.lower())
            else:
                consonants.add(char.lower())
    
    num_vowels = len(vowels)
    num_consonants = len(consonants)
    
    return num_vowels, num_consonants