"""
QUESTION:
Write a function named `avg` that takes an array of integers as input and returns the average of the integers. The function should handle the case where the input array is not empty.
"""

def avg(arr): 
    sum = 0 
    for num in arr:
        sum += num 
    return sum/len(arr)