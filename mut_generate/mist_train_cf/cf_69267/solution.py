"""
QUESTION:
Create a function `contains_sequence` that checks if a given array of integers contains a sequence of numbers with the pattern 123456789, where the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9 appear in exactly that order, with no other numbers in between.
"""

def contains_sequence(arr):
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seq_index = 0
    
    for num in arr:
        if num == sequence[seq_index]:
            seq_index += 1
            if seq_index == len(sequence):
                return True
    return False