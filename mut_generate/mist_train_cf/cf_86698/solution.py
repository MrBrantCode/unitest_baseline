"""
QUESTION:
Write a function named `find_maximum_sum` that takes an array of integers as input and returns the maximum continuous sum that does not include any adjacent elements in the array. The function should also return the subarray that produces this maximum sum. The solution should have a time complexity of O(n) and use constant space.
"""

def find_maximum_sum(arr):
    if len(arr) == 0:
        return 0, []

    maxEndingHere = arr[0]
    maxSoFar = arr[0]
    start = 0
    end = 0

    for i in range(1, len(arr)):
        if arr[i] > maxEndingHere + arr[i]:
            start = i
            maxEndingHere = arr[i]
        else:
            maxEndingHere = maxEndingHere + arr[i]
        
        if maxEndingHere > maxSoFar:
            end = i
            maxSoFar = maxEndingHere

    if maxSoFar < 0:
        return 0, []

    subarray = arr[start:end+1]
    return maxSoFar, subarray