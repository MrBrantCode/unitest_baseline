"""
QUESTION:
Write a function named `count_sum` that calculates the sum of all unique elements in a given list of integers `arr` where 1 <= len(arr) <= 10^6 and -10^6 <= n <= 10^6 for each element `n` in `arr`.
"""

def count_sum(arr):
    '''This function adds all unique elements in ``arr`` and returns the total sum.'''
    unique_elements = set(arr)
    sum = 0
    for n in unique_elements:
        sum += n
    return sum