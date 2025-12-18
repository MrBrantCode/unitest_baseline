"""
QUESTION:
Create a function called `identify_next_number_and_sum` that takes a list of powers of 2 as input and returns a tuple containing the next number in the sequence and the sum of all the numbers in the sequence. The sequence should be less than 1000.
"""

def identify_next_number_and_sum(sequence):
    next_number = sequence[-1] * 2
    sequence_sum = sum(sequence)
    return next_number, sequence_sum