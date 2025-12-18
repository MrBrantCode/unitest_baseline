"""
QUESTION:
Compose a function called `peculiar_sequence` that takes a list of positive whole numbers as input and returns a list of unique numbers that appear less than double their value in the input list. The function should return an empty list if no such numbers exist.
"""

from collections import Counter

def peculiar_sequence(num_series):
    c = Counter(num_series)
    return [num for num, freq in c.items() if freq < 2 * num]