"""
QUESTION:
Generate a function named `generate_fibonacci_sequence` that produces the Fibonacci sequence up to a given number `n`. Each number in the sequence should be the sum of the two preceding ones, starting with 0 and 1. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def generate_fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0, 1]

    while sequence[-1] < n:
        next_num = sequence[-1] + sequence[-2]
        if next_num > n:
            break
        sequence.append(next_num)

    return sequence