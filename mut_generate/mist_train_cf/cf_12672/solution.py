"""
QUESTION:
Design a recursive function `sum_of_squares(n, count=0)` that calculates the sum of the squares of the numbers between 1 and n, and the number of function calls made during the calculation. The function should take an integer `n` as input, convert it to a positive value if necessary, and use a single line of code for the base case.
"""

def entrance(n, count=0):
    n = abs(n)
    if n == 1:
        return 1, count
    else:
        sum_squares, count = entrance(n-1, count+1)
        return sum_squares + n**2, count