"""
QUESTION:
Write a function `findLargestSum(arr)` that takes an array of integers as input and returns the two numbers with the largest sum. The array will have at least two elements and can have up to 10^6 elements. The function should have a time complexity of O(n log n).
"""

def findLargestSum(arr):
    arr.sort()
    maxSum = float('-inf')
    pair = []
    n = len(arr)
    for i in range(n-1, 0, -1):
        currentSum = arr[i] + arr[i-1]
        if currentSum > maxSum:
            maxSum = currentSum
            pair = [arr[i], arr[i-1]]
    return pair