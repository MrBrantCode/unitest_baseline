"""
QUESTION:
Develop a function named `letter_frequency` that calculates the frequency of individual letters and/or characters in a given list of words. The function should take into consideration the case sensitivity of the letters. It should also have options to disregard or include special characters and numbers in the count, and to either return the frequency of all characters or list them in order of their frequency from highest to lowest.
"""

from collections import Counter
from string import ascii_letters

def letter_frequency(words, consider_case=True, include_special_chars=False, sorted_by_freq=False):
    counter = Counter(''.join(words))
    
    if not consider_case:
        counter = Counter(''.join(words).lower())
        
    if not include_special_chars:
        if consider_case:
            counter = Counter(char for char in ''.join(words) if char in ascii_letters)
        else:
            counter = Counter(char.lower() for char in ''.join(words) if char.lower() in ascii_letters)

    if sorted_by_freq:
        return counter.most_common()

    return dict(counter)