"""
QUESTION:
Create a function named `arrayOrder` that takes an array `arr` as input and returns a string indicating whether the array is strictly increasing, strictly decreasing, non-decreasing, non-increasing, or unordered.
"""

def arrayOrder(arr):
    increasing = True
    decreasing = True
    nonDecreasing = False
    nonIncreasing = False
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
            nonIncreasing = False
            if increasing:
                continue
            nonDecreasing = True
        elif arr[i] < arr[i-1]:
            increasing = False
            nonDecreasing = False
            if decreasing:
                continue
            nonIncreasing = True
        else:
            increasing = False
            decreasing = False
    
    if increasing and not nonDecreasing and not nonIncreasing:
        return "Strictly increasing"
    elif decreasing and not nonDecreasing and not nonIncreasing:
        return "Strictly decreasing"
    elif nonDecreasing and not increasing and not decreasing:
        return "Non-decreasing"
    elif nonIncreasing and not increasing and not decreasing:
        return "Non-increasing"
    else:
        return "Unordered"