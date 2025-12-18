"""
QUESTION:
Write a function `count_strings` that takes a list of strings as input and returns the number of strings that start with the letter 'a', have a length greater than 5, and contain at least two vowels and two consonants.
"""

def count_strings(strings):
    count = 0
    
    for string in strings:
        if string.startswith('a') and len(string) > 5:
            vowels = 0
            consonants = 0
            
            for char in string:
                if char.lower() in 'aeiou':
                    vowels += 1
                elif char.isalpha():
                    consonants += 1
                    
            if vowels >= 2 and consonants >= 2:
                count += 1
                
    return count