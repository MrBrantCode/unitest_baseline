"""
QUESTION:
Write a function named `is_arithmetic_progression` that determines whether a given sequence is an arithmetic progression or not. The sequence can have negative numbers and can be of any length, and it may have gaps between elements. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the sequence.
"""

def is_arithmetic_progression(sequence):
    if len(sequence) < 2:
        return True
    
    difference = sequence[1] - sequence[0]
    
    for i in range(1, len(sequence)-1):
        if sequence[i+1] - sequence[i] != difference:
            return False
    
    return True