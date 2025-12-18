"""
QUESTION:
Write a function named `sum_of_cubes` that calculates the sum of the cubes of all numbers from 1 to n. The function should take one integer argument `n` and return the calculated sum. The function should be compatible with Python 3 and should not take any other arguments besides `n`.
"""

def sum_of_cubes(n):
    """
    Calculate the sum of the cubes of all numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the range of numbers.
    
    Returns:
    int: The sum of the cubes of all numbers from 1 to n.
    """
    sum_of_cubes = 0
    for num in range(1, n + 1):
        cube = num ** 3
        sum_of_cubes += cube
    return sum_of_cubes