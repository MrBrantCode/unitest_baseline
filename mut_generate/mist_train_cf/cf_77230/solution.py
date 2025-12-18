"""
QUESTION:
Design a function `lucas(n)` to calculate the Lucas series value at a specific position `n` within the sequence, where the Lucas series is defined as a series of numbers in which each number is the sum of the two preceding numbers, starting from 2 and 1.
"""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas_values = [2, 1]
        for i in range(2, n + 1):
            lucas_values.append(sum(lucas_values[-2:]))
        return lucas_values[n]