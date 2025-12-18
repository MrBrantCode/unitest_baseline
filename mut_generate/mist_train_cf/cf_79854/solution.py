"""
QUESTION:
Write a function `find_element(sequence, digit)` that takes a sequence of numbers and a single digit as input. The function should return the index of the digit in the sequence if it exists, otherwise return -1.
"""

def find_element(sequence, digit):
    try:
        return sequence.index(digit)
    except ValueError:
        return -1