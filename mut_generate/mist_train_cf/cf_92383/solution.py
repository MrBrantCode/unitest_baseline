"""
QUESTION:
Write a function called `count_consonant_vowel_words` that takes a sentence as input and returns the number of words that start with a consonant and end with a vowel, ignoring punctuation and case.
"""

import re

def count_consonant_vowel_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)  # Split the sentence into words
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    count = 0
    for word in words:
        first_letter = word[0].lower()  # Convert the first letter to lowercase for comparison
        last_letter = word[-1].lower()  # Convert the last letter to lowercase for comparison
        
        if first_letter in consonants and last_letter in vowels:
            count += 1
    
    return count