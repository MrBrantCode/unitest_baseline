"""
QUESTION:
Write a function named `eliminate_redundant` that takes a list of integers as input and returns a new list with redundant entries removed. The function should preserve the original order of the sequence.
"""

def eliminate_redundant(sequence):
    result = []
    for i in sequence:
        if i not in result:
            result.append(i)
    return result