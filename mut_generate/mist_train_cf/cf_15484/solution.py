"""
QUESTION:
Write a function `calculate_sum(num)` that uses a recursive approach and only logical and bitwise operators to calculate the sum of all numbers from 1 to `num`. The function should not use the `+` operator or any built-in mathematical functions. The time complexity of the solution should be O(n), where n is the value of `num`.
"""

def calculate_sum(num):
    if num == 1:
        return num
    return calculate_sum(num - 1) - (-num)