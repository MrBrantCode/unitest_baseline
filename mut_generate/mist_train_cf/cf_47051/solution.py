"""
QUESTION:
Design a function `sort_by_binary_len_advanced` that reorders an array of non-negative integers based on the number of bits in their binary representations. The function should have a time complexity of at least O(n log n). In case of equal binary lengths, numbers should be sorted by their decimal values.
"""

def sort_by_binary_len_advanced(arr):
    return sorted(arr, key = lambda x: (bin(x).count('1'), x))