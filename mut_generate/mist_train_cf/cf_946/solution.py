"""
QUESTION:
Write a function `find_maximum_sum(arr)` that takes an array of integers as input and returns the maximum continuous sum that can be achieved by adding the numbers in the array, without including any adjacent elements, along with the subarray that produces the maximum sum. The function should have a time complexity of O(n) and use constant space, and it should handle the case where all elements in the array are negative by returning 0 as the maximum sum and an empty subarray.
"""

def find_maximum_sum(arr):
    if len(arr) == 0:
        return 0, []

    max_ending_here = arr[0]
    max_so_far = arr[0]
    temp = arr[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > temp + arr[i]:
            temp = arr[i]
            temp_start = i
        else:
            temp = temp + arr[i]
        
        if temp > max_ending_here:
            max_ending_here = temp
            start = temp_start
            end = i

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    if max_so_far < 0:
        return 0, []
    
    subarray = arr[start:end+1]
    return max_so_far, subarray