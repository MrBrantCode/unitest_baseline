"""
QUESTION:
Create a function `enhanced_sort_by_binary_len` that takes a list of integers as input, including positive, negative, and zero. The function must sort the list based on the increasing length of the binary representations of the integers. If two integers have the same binary length, they should be sorted based on their decimal values. If a tie still persists, the integers should be sorted based on the count of '1's in their binary representations.
"""

def enhanced_sort_by_binary_len(arr):
    arr.sort(key=lambda x: (len(bin(abs(x)))-2, x, bin(abs(x)).count('1')))
    return arr