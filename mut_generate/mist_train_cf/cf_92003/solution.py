"""
QUESTION:
Create a function called `sum_greater_than_three` that takes a 2D list as input and returns the sum of all values in the list that are greater than 3.
"""

def sum_greater_than_three(lst):
    total_sum = 0
    
    for sublist in lst:
        for value in sublist:
            if value > 3:
                total_sum += value
    
    return total_sum