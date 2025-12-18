"""
QUESTION:
Write a Python function named `find_max_min_average` that takes a sequence of numbers as input. The sequence must contain at least 10 unique numbers. The function should return a tuple containing the maximum number, minimum number, and the average of all the numbers in the sequence.
"""

def find_max_min_average(sequence):
    if len(set(sequence)) < 10:
        return "Sequence must contain at least 10 unique numbers"
    
    max_num = max(sequence)
    min_num = min(sequence)
    average = sum(sequence) / len(sequence)
    
    return max_num, min_num, average