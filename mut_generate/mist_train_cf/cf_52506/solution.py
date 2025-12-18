"""
QUESTION:
Create a function named `fibonacci_sequence` that generates a Fibonacci sequence of a predetermined size `n`. The sequence should start with 0 and 1, and each subsequent number should be the sum of the two preceding ones. The function should take an integer `n` as input and return the Fibonacci sequence as a list of integers. If `n` is less than 2, the function should return an error message indicating that the minimum sequence length is 2.
"""

def fibonacci_sequence(n):
    if n < 2:
        return "Error: The minimum sequence length is 2."

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence