"""
QUESTION:
Write a function called `find_min_difference` that takes a list of integers as input and returns the smallest disparity between any pair of elements within the list. The input list can be modified. The function should have a time complexity of O(n log n) or better.
"""

def find_min_difference(arr):
    arr.sort()

    # Store the minimum difference value
    min_diff = float('inf')
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
        
    return min_diff