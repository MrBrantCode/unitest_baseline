"""
QUESTION:
Create a function named `bitwise_sum` that takes a list of integers as input and returns the sum of all elements in the list using only bitwise operations, with a time complexity of less than O(n^2) and space complexity of O(1) or O(log n). The function should handle both positive and negative integers, duplicate elements, and provide an optimized solution for sorted lists with a time complexity of O(log n).
"""

def bitwise_sum(lst):
    total_sum = 0
    carry = 0
    for num in lst:
        total_sum ^= num
        carry |= total_sum & num
        total_sum &= ~carry
        carry <<= 1
    return total_sum