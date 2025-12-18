"""
QUESTION:
Create a function named `largest_assortment` that takes a string of text as input and returns a list of unique alphanumeric symbols in descending lexicographical order, disregarding case. The function should exclude non-alphanumeric characters and handle duplicate characters.
"""

def largest_assortment(text):
    alphanumeric_symbols = list(sorted(set([c.lower() for c in text if c.isalnum()]), reverse=True))
    return alphanumeric_symbols