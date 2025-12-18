"""
QUESTION:
Write a function `sum_greater_than_three` that takes a 2D list of integers as input and returns the sum of all integers greater than 3.
"""

def sum_greater_than_three(lst):
    total_sum = 0
    
    for sublist in lst:
        for value in sublist:
            if value > 3:
                total_sum += value
    
    return total_sum