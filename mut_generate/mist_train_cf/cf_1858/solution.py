"""
QUESTION:
Write a function `corner_sum` that takes a 2D array of integers as input and returns the sum of all elements that are greater than 10, divisible by 3, and located at the corners of the array, excluding negative numbers. The input array will have at most 100 rows and each row will have at most 100 columns, with values ranging from -1000 to 1000 inclusive.
"""

def corner_sum(array):
    rows = len(array)
    cols = len(array[0])
    sum = 0
    
    # check top left corner
    if array[0][0] > 10 and array[0][0] % 3 == 0 and array[0][0] >= 0:
        sum += array[0][0]
    
    # check top right corner
    if array[0][cols-1] > 10 and array[0][cols-1] % 3 == 0 and array[0][cols-1] >= 0:
        sum += array[0][cols-1]
    
    # check bottom left corner
    if array[rows-1][0] > 10 and array[rows-1][0] % 3 == 0 and array[rows-1][0] >= 0:
        sum += array[rows-1][0]
    
    # check bottom right corner
    if array[rows-1][cols-1] > 10 and array[rows-1][cols-1] % 3 == 0 and array[rows-1][cols-1] >= 0:
        sum += array[rows-1][cols-1]
    
    return sum