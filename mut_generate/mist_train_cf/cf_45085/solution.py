"""
QUESTION:
Create a function `count_vowels` that takes a sequence of alphabetic characters as input and returns the number of vowel phonetic sounds within the sequence. The function should be case-insensitive, treating both lowercase and uppercase vowels as valid. The sequence may contain spaces or other non-alphabetic characters, which should be ignored when counting vowels.
"""

def count_vowels(sequence):
    vowels = 'aeiou'
    sequence = sequence.lower()     #Convert input to lowercase to match the vowels
    count = 0                       #Initialize vowel count
    for char in sequence:
        if char in vowels:
            count += 1              #Increment count if character is a vowel
    return count