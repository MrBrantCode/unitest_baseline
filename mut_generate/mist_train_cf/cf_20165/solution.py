"""
QUESTION:
Write a function `count_substrings(sentence)` that takes a sentence as input and returns the number of substrings of length 3 where the first character is a vowel, the last character is a consonant, and the substrings do not overlap with each other. The vowels are 'a', 'e', 'i', 'o', 'u' and the consonants are all other letters of the alphabet.
"""

def count_substrings(sentence):
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in vowels]
    
    for i in range(len(sentence) - 2):
        if sentence[i] in vowels and sentence[i+2] in consonants:
            counter += 1
    
    return counter