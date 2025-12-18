"""
QUESTION:
Create a function called `perfect_cubes` that takes a positive integer `n` as input and returns a list of all the perfect cubes between 1 and `n` (inclusive), along with the sum of the digits of each perfect cube.
"""

def perfect_cubes(n):
    """
    Returns a list of all perfect cubes between 1 and n (inclusive), 
    along with the sum of the digits of each perfect cube.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        list: A list of tuples, where each tuple contains a perfect cube and 
        the sum of its digits.
    """
    def sum_of_digits(num):
        # Function to calculate sum of digits in a number
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        return sum_digits

    cubes = []
    for i in range(1, n+1):
        cube = i**3
        if cube <= n:
            cubes.append((cube, sum_of_digits(cube)))
    return cubes