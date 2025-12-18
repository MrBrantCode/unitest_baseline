"""
QUESTION:
Generate a function named `generate_list(num)` that takes an integer `num` as input and returns a list of squares of even numbers from 0 to `num` (inclusive), excluding numbers divisible by 10. The list should be sorted in descending order.
"""

def generate_list(num):
    return sorted([i**2 for i in range(0, num+1) if i % 2 == 0 and i % 10 != 0], reverse=True)