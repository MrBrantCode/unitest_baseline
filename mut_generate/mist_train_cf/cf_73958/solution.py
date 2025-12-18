"""
QUESTION:
Write a function called `findFortunateInteger(arr)` that takes an array of integers as input and returns a fortunate integer, which is an integer whose frequency within the array matches its actual numerical value. If multiple fortunate integers exist, return the one with the greatest numerical value. If the array is devoid of any fortunate integers, return -1.

The input array `arr` will have a length between 1 and 500 (inclusive), and each integer in the array will be between 1 and 500 (inclusive).
"""

def findFortunateInteger(arr):
    count_map = {}
    fortunate = -1
    
    for num in arr:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
    
    for num in count_map:
        if num == count_map[num]:
            fortunate = max(fortunate, num)
    
    return fortunate