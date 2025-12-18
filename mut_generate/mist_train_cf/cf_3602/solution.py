"""
QUESTION:
Write a function `count_vowels_and_consonants` that takes a string as input and returns the total number of vowels and consonants, as well as the number of uppercase and lowercase vowels and consonants. The string may contain multiple sentences separated by periods, but should exclude any spaces or punctuation marks except for periods. The function should treat all characters as lowercase for the purpose of counting, and the input string can be modified to remove periods.
"""

def count_vowels_and_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    total_vowels = 0
    total_consonants = 0
    uppercase_vowels = 0
    lowercase_vowels = 0
    uppercase_consonants = 0
    lowercase_consonants = 0
    
    string = string.lower().replace('.', '')  # Converting to lowercase and removing periods
    
    for char in string:
        if char.isalpha():
            if char in vowels:
                total_vowels += 1
                lowercase_vowels += 1
            elif char in consonants:
                total_consonants += 1
                lowercase_consonants += 1
    
    return total_vowels, total_consonants, uppercase_vowels, lowercase_vowels, uppercase_consonants, lowercase_consonants