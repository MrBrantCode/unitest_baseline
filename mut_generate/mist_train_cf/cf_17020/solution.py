"""
QUESTION:
Write a function `sum_of_even_squares` that calculates the sum of the squares of even numbers in a given list. The function must use a single loop to iterate through the list and cannot use built-in Python functions or methods for finding even numbers or calculating squares. Additionally, mathematical operators such as multiplication or exponentiation cannot be used in the solution.
"""

def sum_of_even_squares(lst):
    sum_squares = 0
    for num in lst:
        if (num >> 1) << 1 == num:  
            sum_squares += num - (num - (num >> 1))  
    return sum_squares