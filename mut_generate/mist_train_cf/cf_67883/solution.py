"""
QUESTION:
Create a function named `sort_by_binary_len` that sorts a sequence of integers based on the length of their binary representation. If two integers have the same binary length, the negative integer should appear first, followed by the positive integers. For integers with the same binary length and sign, sort them in ascending order.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key=lambda x: (len(bin(abs(x)))-2, x >= 0, x))