"""
QUESTION:
Write a function `find_median` that calculates the median of an array of integers. The input array will contain n elements, where n is a positive integer not exceeding 10^6. The function should not modify the input array, and its time and space complexities should not exceed O(nlogn) and O(n), respectively.
"""

def find_median(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    
    if n % 2 == 0:
        median = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        median = sorted_arr[n//2]
    
    return median