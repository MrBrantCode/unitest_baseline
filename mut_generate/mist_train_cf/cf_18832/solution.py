"""
QUESTION:
Write a function `find_maximum` that takes a list of integers as input and returns the maximum value among them. The function should have a time complexity of O(n), where n is the number of integers in the list, and should handle negative numbers. Do not use any built-in Python functions or libraries.
"""

def find_maximum(numbers):
    max_value = float('-inf')
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value