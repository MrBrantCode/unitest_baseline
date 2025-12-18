"""
QUESTION:
Write a function called `sum_2d_array` that calculates the sum of all elements in a given 2-dimensional array. The input array is a list of lists where each inner list represents a row in the 2D array. The function should return the total sum of all elements.
"""

def sum_2d_array(arr):
    result = 0
    for row in arr:
        for num in row:
            result += num
    return result