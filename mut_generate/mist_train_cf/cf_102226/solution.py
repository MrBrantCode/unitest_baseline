"""
QUESTION:
Write a function `calculate_sum` that takes a list of integers as input and returns the sum of the integers without using any built-in functions or methods for sum calculation. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def calculate_sum(lst):
    total_sum = 0
    for num in lst:
        total_sum += num
    return total_sum