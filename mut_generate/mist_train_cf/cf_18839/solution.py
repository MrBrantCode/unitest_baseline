"""
QUESTION:
Given an int array A with at least two elements, write a function `findMinDifference(A)` to find the pair of elements with the minimum absolute difference. The solution should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def findMinDifference(A):
    A.sort() # Sort the array in ascending order
    
    minDiff = float('inf') # Initialize minDiff to a large value
    minPair = [] # Initialize minPair to an empty array
    
    for i in range(1, len(A)):
        diff = abs(A[i] - A[i-1]) # Calculate the absolute difference
        
        if diff < minDiff:
            minDiff = diff
            minPair = [A[i-1], A[i]]
    
    return minPair