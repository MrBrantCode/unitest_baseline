"""
QUESTION:
Create a function `find_term(sequence, term)` that checks if a given term exists within a supplied sequence of alphanumeric symbols. The function should consider the case sensitivity of the term. The function should return `True` if the term exists in the sequence, and `False` otherwise.
"""

def find_term(sequence, term):
    if term in sequence:
        return True
    else:
        return False