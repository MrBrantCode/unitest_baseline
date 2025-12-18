"""
QUESTION:
Create a function `count_vowels` that takes a string as input and returns the total number of vowels in the string, considering both uppercase and lowercase vowels, excluding any vowels that occur as part of a consonant cluster (i.e., a group of consonants with no vowels in between).
"""

def entrance(string):
    vowels = "aeiou"
    count = 0
    previous_char = ''
    
    for char in string:
        char = char.lower()
        
        if char in vowels:
            if previous_char in vowels:
                count -= 1
            count += 1
        
        previous_char = char
    
    return count