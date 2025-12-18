"""
QUESTION:
Given an array of up to 10^6 elements with possible duplicate and negative values, and a target number within the range of -10^9 to 10^9, write a function named `closest_pair(arr, target)` to find the pair of elements in the array that have the smallest absolute difference with the target number. If multiple pairs have the same smallest absolute difference, return any one of them.
"""

def closest_pair(arr, target):
    arr.sort()  
    min_diff = float('inf')  
    result = [0, 0]  

    for i in range(len(arr) - 1):
        diff = abs(arr[i] + arr[i+1] - target)  
        if diff < min_diff:
            min_diff = diff
            result = [arr[i], arr[i + 1]]
            
    return result