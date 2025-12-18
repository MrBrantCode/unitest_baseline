"""
QUESTION:
Develop a function named `find_pivot` that takes a list of integers as input and returns the index of the "pivot" element. The pivot element is the unique element for which the sum of all elements to its left equals the average of all distinct elements to its right. If no such element exists, the function should return -1. The function should handle cases where the sum of the remaining elements on the right side is zero.
"""

def find_pivot(lst):
    total_sum = sum(lst)
    left_sum = 0
    for i, num in enumerate(lst):
        total_sum -= num
        if left_sum == total_sum / (len(lst) - i - 1 if len(lst) - i - 1 > 0 else 1):
            return i
        left_sum += num
    return -1