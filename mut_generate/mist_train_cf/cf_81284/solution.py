"""
QUESTION:
Create a function `count_elements` that takes a string of alphanumeric symbols as input. The function should return the total count of vowels, consonants, digits, spaces, and special characters in the string, as well as the frequency of each individual character. The function should treat the input string as case-insensitive.
"""

def count_elements(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    space_count = 0
    special_count = 0
    char_frequency = {}
    
    for char in input_string.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
        elif char.isnumeric():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            special_count += 1
            
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
            
    result = {
        "vowels": vowel_count,
        "consonants": consonant_count,
        "digits": digit_count,
        "spaces": space_count,
        "special_characters": special_count,
        "character_frequency": char_frequency
    }
    return result