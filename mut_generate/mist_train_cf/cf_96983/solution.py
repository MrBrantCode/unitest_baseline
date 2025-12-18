"""
QUESTION:
Create a function `findMax` that takes an array of integers `arr` as input and returns the maximum element in the array. The array will contain at least 2 elements and at most 10^6 elements, and each element will be an integer between -10^9 and 10^9.
"""

def findMax(arr):
    maxElement = arr[0]
    for num in arr[1:]:
        if num > maxElement:
            maxElement = num
    return maxElement