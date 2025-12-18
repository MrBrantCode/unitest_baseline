"""
QUESTION:
Write a function `vowels_followed_by_consonant` that takes a sentence as input and returns True if all the vowels in the sentence are followed by a consonant, False otherwise. The function should be case-insensitive and consider only alphabetic characters.
"""

def vowels_followed_by_consonant(sentence):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    sentence = sentence.lower()
    
    for i in range(len(sentence)-1):
        if sentence[i] in vowels and sentence[i+1] not in consonants:
            return False
    
    return True