"""
QUESTION:
Write a function named `findPairs` that takes two inputs, an array of integers and a target integer, and returns the number of pairs of elements in the array that sum up to the target value. The function should assume that the input array contains at least two elements and may contain duplicate values. The function should return the count of pairs, not the pairs themselves.
"""

def findPairs(arr, target):
    arr.sort()  # Sort the array in ascending order
    count = 0
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] == target:
            count += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    
    return count