"""
QUESTION:
Write a function `calculateSum` that takes in an array of integers `arr` and returns the sum of all the positive integers in the array. The function should return 0 if the array is empty or contains no positive integers.
"""

def calculateSum(arr):
    result = 0
    for num in arr:
        if num > 0:
            result += num
    return result