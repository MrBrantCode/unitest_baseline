"""
QUESTION:
Write a function `findSmallestMissingPositiveNumber` that takes an array of integers as input and returns the smallest positive integer missing from the array. The function must run in O(N) time complexity and O(1) space complexity, where N is the size of the array. The array can contain integers ranging from -10^9 to 10^9. If all positive integers up to N are present in the array, the function should return N+1.
"""

def findSmallestMissingPositiveNumber(arr):
    N = len(arr)
    
    # Mark the presence of positive numbers
    for i in range(N):
        num = abs(arr[i])
        if num <= N:
            arr[num-1] = -abs(arr[num-1])
    
    # Find the first index with a positive number
    for i in range(N):
        if arr[i] > 0:
            return i+1
    
    # No positive number found, return N+1
    return N+1