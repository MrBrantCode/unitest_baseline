"""
QUESTION:
Write a function `find_anomaly` that takes a list of integers as input and returns the first integer that appears a different number of times than the other integers. If all integers appear the same number of times, return None.
"""

def find_anomaly(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in arr:
        if count[num] != count[arr[0]]:
            return num

    return None