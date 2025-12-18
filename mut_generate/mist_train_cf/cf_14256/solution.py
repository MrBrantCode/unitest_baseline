"""
QUESTION:
Write a function named `tribonacci_sequence` that generates a sequence of numbers where each number is the sum of the three preceding numbers, starting with 0, 1, and 1, and returns the first n numbers in the sequence. The function should take an integer n as input and return a list of integers.
"""

def tribonacci_sequence(n):
    """
    Generates a sequence of numbers where each number is the sum of the three preceding numbers,
    starting with 0, 1, and 1, and returns the first n numbers in the sequence.

    Args:
        n (int): The number of elements in the sequence to generate.

    Returns:
        list: A list of integers representing the Tribonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n == 3:
        return [0, 1, 1]
    else:
        sequence = [0, 1, 1]
        while len(sequence) < n:
            sequence.append(sum(sequence[-3:]))
        return sequence