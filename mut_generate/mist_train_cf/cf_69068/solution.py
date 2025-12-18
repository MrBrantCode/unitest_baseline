"""
QUESTION:
Write a function `match_sentence(sentence)` that returns `True` if the input sentence contains the word "dog", followed by any number of characters except the letters "x" and "y", and ends with the word "cat" followed by a non-prime number between 1 and 10 inclusive. The words "dog" and "cat" should not be part of another word.
"""

import re

def match_sentence(sentence):
    non_prime_numbers = [1, 4, 6, 8, 9, 10]   
    for num in non_prime_numbers:
        pattern = r"\bdog[^xy]*\bcat" + str(num) + r"\b" 
        match = re.fullmatch(pattern, sentence)
        if match:
            return True
    return False