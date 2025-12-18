"""
QUESTION:
Create a function called `count_uppercase_vowels` that takes a string of English words as input and returns the total count of uppercase vowels in the string. The function should only consider the characters 'A', 'E', 'I', 'O', and 'U' as vowels.
"""

def count_uppercase_vowels(sentence):
    vowels = 'AEIOU'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count