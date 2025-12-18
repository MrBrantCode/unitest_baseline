"""
QUESTION:
Write a function `find_median(arr)` to find the median of a sorted array. The function should take a sorted list of numbers as input and return the median of the array. If the array has an even length, the median is the average of the two middle elements; if the array has an odd length, the median is the middle element.
"""

def find_median(arr):
    n = len(arr)
    
    if n % 2 == 0:  # If the array has even length
        mid = n // 2
        median = (arr[mid] + arr[mid - 1]) / 2
    else:  # If the array has odd length
        mid = n // 2
        median = arr[mid]
    
    return median