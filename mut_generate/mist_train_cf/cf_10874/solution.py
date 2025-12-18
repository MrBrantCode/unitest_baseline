"""
QUESTION:
Write a function called `fibonacci_sequence` that generates the Fibonacci sequence up to a given number `n`. The function should take an integer `n` as input and return a list of Fibonacci numbers that do not exceed `n`. The sequence should start with 0 and 1.
"""

def entance(n):
    sequence = [0, 1]  # initialize the sequence with the first two numbers: 0 and 1

    # calculate subsequent Fibonacci numbers until reaching the given number
    while sequence[-1] + sequence[-2] <= n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence