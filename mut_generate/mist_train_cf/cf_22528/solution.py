"""
QUESTION:
Write a function `calculate_sum_except_self(arr)` that takes an array of integers and returns a new array of the same size, where each element is the sum of all elements in the original array except itself. The solution should have a time complexity of O(n) and a space complexity of O(1), without modifying the input array.
"""

def calculate_sum_except_self(arr):
    total_sum = sum(arr)
    result = []
    for num in arr:
        result.append(total_sum - num)
    return result