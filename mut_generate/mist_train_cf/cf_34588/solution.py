"""
QUESTION:
Given a list of integers where every number appears an even number of times except for one, write a function `findOdd(arr)` to find the integer that appears an odd number of times. The function should take a list of integers as input and return the integer that appears an odd number of times.
"""

def findOdd(arr):
    result = 0
    for num in arr:
        result ^= num
    return result