"""
QUESTION:
Write a function called `evaluate_word_sets_order_and_frequency` that takes two string parameters and returns a boolean value indicating whether the unique alphanumeric words in both strings are identical, ignoring case and non-alphanumeric characters, and considering their order and frequency.
"""

import re

def evaluate_word_sets_order_and_frequency(phrase1: str, phrase2: str) -> bool:
    p1 = re.sub("[^\w]", " ",  phrase1).lower().split()
    p2 = re.sub("[^\w]", " ",  phrase2).lower().split()
    return p1 == p2