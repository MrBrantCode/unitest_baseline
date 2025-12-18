"""
QUESTION:
Write a function `longestIncreasingSubsequence` that takes an array of integers as input and returns the length of the longest increasing subsequence within the array. The function should have a time complexity of O(n^2) or better, where n is the number of elements in the array.
"""

def longestIncreasingSubsequence(arr):
    n = len(arr)
    lis = [1]*n

    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1

    maximum = 0
    for i in range(len(lis)):
        maximum = max(maximum , lis[i])

    return maximum