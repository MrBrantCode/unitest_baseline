"""
QUESTION:
Write a function named `fibonacci_sequence` that prints the Fibonacci sequence up to the 20th element, where each number is the sum of the two preceding ones.
"""

def fibonacci_sequence(n=20):
    """
    Prints the Fibonacci sequence up to the nth element.

    Args:
        n (int): The number of elements in the Fibonacci sequence. Defaults to 20.
    """
    a, b = 0, 1
    sequence = [a, b]
    while len(sequence) < n:
        c = a + b
        sequence.append(c)
        a, b = b, c
    return sequence

# Removed the test case to print the sequence