"""
QUESTION:
Write a function called `sum_absolute_values` that takes two arrays of integers as input. Each array has a length between 1 and 1000, and the sum of the elements in each array does not exceed 10^6. The function should return the sum of the absolute values of the elements in both arrays. If either of the input arrays is empty, the function should return -1.
"""

def sum_absolute_values(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return -1
    else:
        sum = 0
        for num in array1:
            sum += abs(num)
        for num in array2:
            sum += abs(num)
        return sum