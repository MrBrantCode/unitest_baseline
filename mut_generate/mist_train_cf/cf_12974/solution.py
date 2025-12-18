"""
QUESTION:
Write a function called `generate_list` that takes an integer `n` as input and returns a list of integers from 1 to `n` (inclusive) without using any built-in functions or libraries. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def generate_list(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers