"""
QUESTION:
Write a function called `sum_of_squares` to calculate the sum of the squares of the first n natural numbers without using the built-in sum() function. The function should use a nested loop structure. The input n should be a positive integer.
"""

def sum_of_squares(n):
    """
    Calculate the sum of the squares of the first n natural numbers.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of the squares of the first n natural numbers.
    """
    sum_of_squares = 0
    for i in range(1, n+1):  
        for j in range(1, i+1):  
            sum_of_squares += j ** 2  
    return sum_of_squares