"""
QUESTION:
Write a function called `sum_of_absolute_values` that takes two arrays of integers as input and returns the sum of the absolute values of the elements in both arrays. The arrays have a length between 1 and 1000 and may contain both positive and negative integers. If either array is empty, the function should return -1.
"""

def sum_of_absolute_values(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return -1
    
    sum1 = sum(abs(num) for num in array1)
    sum2 = sum(abs(num) for num in array2)
    
    return sum1 + sum2