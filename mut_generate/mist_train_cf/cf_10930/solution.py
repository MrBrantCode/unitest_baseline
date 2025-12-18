"""
QUESTION:
Write a function `findLargestSumSubarray` that takes an integer array as input and returns the subarray with the largest sum, consisting of consecutive elements. The function must have a time complexity of O(n) and a space complexity of O(1). The input array may contain negative numbers.
"""

def findLargestSumSubarray(arr):
    maxSoFar = float('-inf')
    maxEndingHere = 0
    start = 0
    end = 0

    for i in range(len(arr)):
        maxEndingHere += arr[i]
        
        if maxEndingHere < arr[i]:
            maxEndingHere = arr[i]
            start = i
        
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            end = i

    return arr[start:end+1]