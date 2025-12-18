"""
QUESTION:
Construct a function called `generate_sequence(n)` that generates a unique Fibonacci-like sequence of numbers where each number is the sum of the previous three numbers. The sequence should start with the numbers 0, 1, and 1, and return a list of the first n numbers in the sequence.
"""

def generate_sequence(n):
    sequence = [0, 1, 1]
    
    for i in range(3, n):
        sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])

    return sequence