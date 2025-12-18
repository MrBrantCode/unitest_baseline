"""
QUESTION:
Create a function named `is_five_alpha` that takes a string `nomenclature` as input and returns a boolean value. The function should return `True` if the length of the string is exactly 5 and all characters are alphabetic, and `False` otherwise.
"""

def is_five_alpha(nomenclature):
    return len(nomenclature) == 5 and nomenclature.isalpha()