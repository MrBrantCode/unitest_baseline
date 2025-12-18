"""
QUESTION:
Write a function `findSum` that takes an array of integers as input and returns the sum of the two largest numbers in the array using a recursive approach, without using any built-in sorting functions or loops.
"""

def findSum(arr, i, max1=float('-inf'), max2=float('-inf')):
    # Base Case
    if i == len(arr):
        return max1 + max2
    
    # Recursive Case
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
    elif arr[i] > max2:
        max2 = arr[i]
    
    return findSum(arr, i + 1, max1, max2)