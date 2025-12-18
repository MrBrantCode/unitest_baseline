"""
QUESTION:
Create a program with two functions: `fibonacci(n)` and `odd_numbers(sequence)`. The `fibonacci(n)` function generates a set of Fibonacci sequence numbers with a length equal to the positive integer `n`, where `n` is between 1 and 20, inclusive. The sequence starts with the numbers 1 and 1 for the first and second terms. The `odd_numbers(sequence)` function creates a new set containing only the odd numbers from the Fibonacci sequence. Validate user's input and handle possible exceptions.
"""

def fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n > 2:
        sequence = [1, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence

def odd_numbers(sequence):
    return [num for num in sequence if num % 2 != 0]