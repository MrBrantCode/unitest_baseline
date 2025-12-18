"""
QUESTION:
Write a function `fibonacci_sequence(n)` that computes the Fibonacci sequence up to a given number `n`, where `n` is a positive integer less than or equal to 1000. The function should have a time complexity of O(n) and a space complexity of O(1), take an integer `n` as input, and return a list containing the Fibonacci sequence up to the nth number, where each subsequent number is the sum of the two preceding numbers (with the first and second numbers being 1).
"""

def fibonacci_sequence(n):
    sequence = [1, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]