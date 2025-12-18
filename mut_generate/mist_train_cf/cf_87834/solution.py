"""
QUESTION:
Create a function called `check_string` that takes a single string argument. The function should return `True` if the string contains all vowels in alphabetical order without repetition, has an equal number of consonants and vowels, and meets the following conditions: 
- The string length is less than or equal to 100 characters.
- The string only contains letters (no numbers or special characters).
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