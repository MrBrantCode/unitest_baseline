"""
QUESTION:
Write a function `count_strings(strings)` that takes a list of strings as input and returns the number of strings that start with the letter 'a', have a length greater than 5, contain at least three unique vowels (aeiou), and contain at least three unique consonants (non-vowels). The function should be case-insensitive.
"""

def count_strings(strings):
    count = 0
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    for string in strings:
        if string[0].lower() == 'a' and len(string) > 5:
            vowel_count = 0
            consonant_count = 0
            
            for char in string.lower():
                if char in vowels:
                    vowel_count += 1
                elif char in consonants:
                    consonant_count += 1
            
            if vowel_count >= 3 and consonant_count >= 3:
                count += 1
    
    return count