"""
QUESTION:
Design a function named `find_median` that calculates the median of three input arrays of integers. Each array can contain from 0 to 10^5 integers. The function should have a time complexity of O(n log n).
"""

def find_median(arr1, arr2, arr3):
    merged = arr1 + arr2 + arr3
    sorted_merged = sorted(merged)
    
    n = len(sorted_merged)
    if n % 2:  # it means n is odd
        return sorted_merged[n // 2]
    else:
        mid1, mid2 = sorted_merged[(n-1) // 2], sorted_merged[n // 2]
        return (mid1 + mid2) / 2.0