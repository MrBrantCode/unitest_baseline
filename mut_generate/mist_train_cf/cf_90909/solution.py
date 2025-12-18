"""
QUESTION:
Write a function named `find_odd_number` that takes a list of integers as input and returns the first integer that appears an odd number of times in the list. If no integer appears an odd number of times, return -1.
"""

def find_odd_number(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in arr:
        if count[num] % 2 == 1:
            return num

    return -1