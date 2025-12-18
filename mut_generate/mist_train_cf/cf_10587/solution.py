"""
QUESTION:
Create a function named `fibonacci_sequence` that takes an integer `length` as input, where `length` must be at least 5. The function should generate a Fibonacci sequence of the given length and print the sequence as well as the sum of all numbers in the sequence.
"""

def fibonacci_sequence(length):
    """
    Generate a Fibonacci sequence of the given length and calculate the sum of all numbers in the sequence.

    Args:
        length (int): The length of the Fibonacci sequence. Must be at least 5.

    Returns:
        tuple: A tuple containing the Fibonacci sequence and the sum of its numbers.
    """
    sequence = [0, 1]
    sum_sequence = 1
    
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        sum_sequence += next_number
    
    return sequence, sum_sequence