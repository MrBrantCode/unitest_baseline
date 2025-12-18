"""
QUESTION:
Design a function named `count_consonants` that calculates the total number of consonants from a given list of sentences. The function should exclude sentences that start with a vowel, end with a consonant, or contain any special characters. Additionally, it should exclude sentences that contain numbers, are less than 5 words long, or have more than 10 words. The function should handle case sensitivity and sentences with punctuation marks, and return the sentence with the highest number of consonants.
"""

import re

def count_consonants(sentences):
    vowels = 'AEIOUaeiou'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    total_consonants = 0
    max_consonants = 0
    max_consonant_sentence = ''
    
    for sentence in sentences[:]: 
        words = sentence.split()
        if len(words) < 5 or len(words) > 10:
            continue
        if sentence[0] in vowels and sentence[-1] in vowels:
            if re.match('^[A-Za-z ]*$', sentence) is not None: 
                count = 0
                for letter in sentence:
                    if letter in consonants:
                        count += 1
                        total_consonants += 1
                # Check if this sentence has the highest consonants
                if max_consonants < count:
                    max_consonants = count
                    max_consonant_sentence = sentence
    return total_consonants, max_consonant_sentence