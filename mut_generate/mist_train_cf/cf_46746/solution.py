"""
QUESTION:
Create a function named `sum_array` that calculates the cumulative total of all numerical elements in a given array. The function should take one parameter, `array`, and return the total sum of its elements. Assume that the input array contains only numerical values.
"""

def sum_array(array):
    total = 0
    for num in array:
        total += num
    return total