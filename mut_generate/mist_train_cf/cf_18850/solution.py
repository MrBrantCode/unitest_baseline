"""
QUESTION:
Create a function `is_arithmetic_progression` that takes a sequence of integers as input and returns a boolean value indicating whether the sequence is an arithmetic progression. The sequence can have negative numbers, be of any length, and may have missing elements. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the sequence.
"""

def is_arithmetic_progression(sequence):
    if len(sequence) < 2:
        return True
    
    difference = sequence[1] - sequence[0]
    
    for i in range(1, len(sequence)-1):
        if sequence[i+1] - sequence[i] != difference:
            return False
    
    return True