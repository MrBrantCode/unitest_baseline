"""
QUESTION:
Create a function named `sort_by_binary_one_count` that sorts a list of non-negative integers in ascending order based on the count of '1's in their binary representation. If integers have the same count of '1's, they should be sorted by their decimal values.
"""

def sort_by_binary_one_count(arr): 
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))