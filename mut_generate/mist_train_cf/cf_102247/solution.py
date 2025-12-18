"""
QUESTION:
Create a function called `sum_values_greater_than_five` that takes a 2D list as input and returns the sum of all values greater than 5. The function should only consider values that are greater than 5 and ignore all other values.
"""

def sum_values_greater_than_five(lst):
    sum = 0
    for row in lst:
        for element in row:
            if element > 5:
                sum += element
    return sum