"""
QUESTION:
Generate a function named `generate_fibonacci_sequence(n)` that takes an integer `n` as input and returns a list of Fibonacci numbers where the last number in the list is less than `n`. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The input `n` is guaranteed to be greater than or equal to 2.
"""

def generate_fibonacci_sequence(n):
    """
    Generate a list of Fibonacci numbers where the last number in the list is less than 'n'.

    Args:
        n (int): The input number up to which the Fibonacci sequence is generated.

    Returns:
        list: A list of Fibonacci numbers.
    """
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    
    while sequence[-1] + sequence[-2] < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence