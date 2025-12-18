"""
QUESTION:
Create a function `closest_pair(arr, target)` that takes a list of integers `arr` with at most 10^6 elements and an integer `target` within the range of -10^9 to 10^9 as input, and returns a pair of elements in `arr` with the smallest absolute difference with `target`. If multiple pairs have the same smallest absolute difference, return any one of them. The function should work with unsorted arrays containing duplicate, positive, and negative elements.
"""

def closest_pair(arr, target):
    arr.sort()  
    min_diff = float('inf')  
    result = [0, 0]  

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - target)  
        if diff < min_diff:
            min_diff = diff
            result = [arr[i], arr[i + 1]]

    return result