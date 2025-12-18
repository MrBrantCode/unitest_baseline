"""
QUESTION:
Create a function `check_string(string)` that takes a string as input and returns `True` if the string meets the following conditions: it contains all the vowels in alphabetical order without repetition, it has an equal number of consonants and vowels, its length is less than or equal to 100 characters, and it only contains letters. Otherwise, the function should return `False`.
"""

def check_string(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()  # convert string to lowercase
    
    # Check if string length is less than or equal to 100
    if len(string) > 100:
        return False
    
    # Check if string contains only letters
    if not string.isalpha():
        return False
    
    # Check if string contains all vowels in alphabetical order without repetition
    vowel_order = ''
    for char in string:
        if char in vowels and char not in vowel_order:
            vowel_order += char
    if vowel_order != 'aeiou':
        return False
    
    # Check if the number of consonants is equal to the number of vowels
    vowel_count = sum(1 for char in string if char in vowels)
    consonant_count = len(string) - vowel_count
    if vowel_count != consonant_count:
        return False
    
    return True