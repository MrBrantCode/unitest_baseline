"""
QUESTION:
Write a function `find_kth_smallest(arr, k)` that takes an array of integers and an integer `k` as input, and returns a tuple containing the kth smallest unique element in the array and its frequency. If `k` is larger than the number of unique elements in the array, return an error message. Assume `k` is 1-indexed.
"""

import collections
import heapq

def find_kth_smallest(arr, k):
    if k > len(arr):
        return 'Error: k is larger than the array length.'
    
    unique_values = list(set(arr))
    
    if k > len(unique_values):
        return 'Error: k is greater than the number of unique elements in the array.'
    
    kth_smallest = heapq.nsmallest(k, unique_values)[-1]
    
    count = collections.Counter(arr)[kth_smallest]
    
    return (kth_smallest, count)