"""
QUESTION:
Write a function called `is_pangram` that takes a string as input and returns a boolean value indicating whether the string is a pangram (a sentence that contains every letter of the alphabet at least once). The function should ignore non-alphabetic characters and be case-insensitive.
"""

def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    # Create a set of all the alphabetic characters in the sentence
    chars = set(c for c in sentence if c.isalpha())
    # Check if the set has 26 characters (i.e., all the letters of the alphabet)
    return len(chars) == 26