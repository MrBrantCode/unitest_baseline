"""
QUESTION:
Implement a function called `find_even_indices` that takes an array of integers as input and returns a list of indices where the corresponding elements are even numbers. The array may contain both positive and negative integers, and the output indices should be in ascending order. The solution should have a time complexity of O(n) and a space complexity of O(1), without using built-in functions or methods that directly identify even numbers or check for divisibility by 2.
"""

def find_even_indices(nums):
    result = []
    for i, num in enumerate(nums):
        if abs(num) % 2 == 0:
            result.append(i)
    return sorted(result)