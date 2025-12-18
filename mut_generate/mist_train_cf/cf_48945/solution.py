"""
QUESTION:
Construct a function named `count_consonants` that takes a list of sentences as input. The function should count the total number of consonants from the sentences, excluding those that start with a vowel, end with a consonant, contain numbers, or have less than 5 words.
"""

import string

def count_consonants(sentences):
    total_consonants = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    
    for sentence in list(sentences): 
        if any(char.isdigit() for char in sentence):
            continue
        words = sentence.lower().split() 
        if len(words) < 5 or words[0][0] in vowels or words[-1][-1] in consonants:
            continue
        else:
            total_consonants += sum(1 for word in words for char in word if char in consonants)
    return total_consonants