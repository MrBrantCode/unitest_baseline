"""
QUESTION:
Design a function `factorial_append(tup, list)` that calculates the factorial of each element in the given tuple `tup`, rounds floating point numbers to the nearest integer before calculation, handles tuples containing zero and negative numbers, and appends the results to the given list. The function should return an error message if the tuple is empty.
"""

import math 

def factorial_append(tup, list):
    # Function to handle factorial of floating point or negative numbers
    def factorial(n):
        if n < 0:
            return "ERROR: Negative number"
        elif n == 0 or n == 1:
            return 1
        else:
            return math.factorial(n)

    # Check if tuple is empty
    if not tup:
        return "ERROR: The tuple is empty"
        
    # Loop through the tuple, calculate the factorial and append it to the list
    for i in tup:
        n = round(i)    # Round floating point numbers to the nearest integer
        res = factorial(n)
        list.append(res)   # Append the result to the list
        
    return list