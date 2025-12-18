"""
QUESTION:
Write a function `generate_fibonacci_sequence(n)` to generate the Fibonacci sequence up to a given number `n`, where each number in the sequence is the sum of the two preceding ones, starting with 0 and 1. The function should have a time complexity of O(n) and a space complexity of O(1), and it should return the sequence as a list.
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