"""
QUESTION:
Create a function called `count_strings` that takes a list of strings as input and returns the number of strings that start with the letter 'a' (ignoring case), have a length greater than 5, and contain at least three unique vowels and three unique consonants (non-vowel characters).
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