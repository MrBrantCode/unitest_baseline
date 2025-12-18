"""
QUESTION:
Write a function named `lucas_numbers` that generates the first N Lucas numbers, where the Lucas sequence is defined by the recurrence relation L_n = L_(n-1) + L_(n-2) with initial values L0 = 2 and L1 = 1. The function should return a list of integers representing the first N Lucas numbers. The input N is a positive integer, and the function should handle cases where N is 0, 1, or 2 separately.
"""

def lucas_numbers(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 1]
    else:
        sequence = [2, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence