"""
QUESTION:
Design a function named `sort_by_binary_len` that takes an array of positive integers, negative integers, and floating-point numbers as input. The function should return the array sorted in ascending order based on the lengths of their positive binary equivalents. If two numbers have the same binary length, integers should be sorted by their absolute decimal values, while floating-point numbers should be sorted by their pure decimal values. The function should handle negative values without changing their sign.
"""

def sort_by_binary_len(arr):
    def binary_len(n):
        if n == 0:
            return 0
        else:
            return len(bin(int(abs(n)))) - 2

    arr.sort(key=lambda x: (binary_len(x), abs(x) if isinstance(x, int) else x))
    return arr