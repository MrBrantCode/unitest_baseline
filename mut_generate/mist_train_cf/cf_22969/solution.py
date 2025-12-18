"""
QUESTION:
Write a function called `findLargestSum` that finds the two numbers in a given array with the largest sum. The array can contain both positive and negative numbers and has at least two elements. The function should have a time complexity of O(n log n).
"""

def findLargestSum(arr):
    arr.sort()
    maxSum = float('-inf')
    currentSum = float('-inf')
    pair = []
    
    n = len(arr)
    for i in range(n-1, 0, -1):  
        currentSum = arr[i] + arr[i-1]
        
        if currentSum > maxSum:
            maxSum = currentSum
            pair = [arr[i], arr[i-1]]
    
    return pair