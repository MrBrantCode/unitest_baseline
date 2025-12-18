"""
QUESTION:
Implement the `longest_increasing_subsequence` function to calculate the length of the longest increasing subsequence in a given array using dynamic programming. The function should take an array of integers as input and return the length of the longest increasing subsequence. The time complexity should be O(n^2) and the space complexity should be O(n), where n is the number of elements in the array.
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1

    max_length = 0
    for i in range(len(lis)):
        max_length = max(max_length, lis[i])

    return max_length