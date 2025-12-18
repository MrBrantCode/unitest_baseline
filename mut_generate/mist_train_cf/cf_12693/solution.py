"""
QUESTION:
Write a function named `calculate_sum` that takes an integer `num` as input and returns the sum of all multiples of 3 and 5 between 1 and `num` (inclusive), excluding any numbers that are multiples of both 3 and 5.
"""

def calculate_sum(num):
    total_sum = 0
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum