"""
QUESTION:
Write a function `generate_fibonacci(n)` that generates a Fibonacci sequence up to the `n-th` number using recursion and another function `validate_fibonacci(sequence)` that validates the Fibonacci sequence using a loop. The generated sequence must be a list of integers and the validation function should return `True` if the sequence is valid and `False` otherwise. The `n` in `generate_fibonacci(n)` is a non-negative integer. The `sequence` in `validate_fibonacci(sequence)` is a list of integers.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = generate_fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

def validate_fibonacci(sequence):
    if len(sequence) <= 2:
        return sequence == [0] or sequence == [0, 1]

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + sequence[i-2]:
            return False
    return True