"""
QUESTION:
Write a function `min_decreasing_subseq(arr)` to find the minimum length of the shortest consecutive strictly decreasing subsequence in the given array `arr`. The function should have a time complexity less than O(n^2), where n is the number of elements in the array.
"""

def min_decreasing_subseq(arr):
    n = len(arr)
    min_length = float('inf')
    count = 1

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            count += 1
        else:
            min_length = min(min_length, count)
            count = 1
            
    min_length = min(min_length, count)
    
    return min_length