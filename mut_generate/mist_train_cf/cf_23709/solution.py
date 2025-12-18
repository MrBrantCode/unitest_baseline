"""
QUESTION:
Create a function called `letter_count` that takes a string as input. The function should return a dictionary where each key is a letter of the alphabet (a-z) and the corresponding value is the number of times that letter appears in the input string. The function should be case-insensitive.
"""

def letter_count(string):
    string = string.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counts = {letter: 0 for letter in alphabet}
    
    for letter in string:
        if letter in alphabet:
            counts[letter] += 1
    
    return counts