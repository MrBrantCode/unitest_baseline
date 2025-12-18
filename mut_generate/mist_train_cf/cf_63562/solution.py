"""
QUESTION:
Create a function named `rollingMax` that takes a list of integers as input. The function should return a list of the maximum element found until the current point in the sequence. If the input list contains any negative integers, the function should return an empty list.
"""

def rollingMax(arr):
    result = []
    maxNum = float('-inf')
  
    for i in arr:
        if i < 0:    # if negative element found, return empty list
            return []
        else:
            maxNum = max(i, maxNum)
            result.append(maxNum)
    return result