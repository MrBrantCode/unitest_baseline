"""
QUESTION:
Write a function named `generate_fibonacci_and_cubes` that generates the first n Fibonacci numbers and their corresponding perfect cubes with a time complexity less than O(n^2). The function should return two lists: one for Fibonacci numbers and one for their corresponding perfect cubes.
"""

def generate_fibonacci_and_cubes(n):
    """
    Generates the first n Fibonacci numbers and their corresponding perfect cubes.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        tuple: A tuple of two lists. The first list contains the Fibonacci numbers, 
               and the second list contains their corresponding perfect cubes.
    """
    a, b = 0, 1
    fibonacci_numbers = [a, b]
    cubes = [a**3, b**3]

    for _ in range(n - 2):  # Loop to calculate the rest of the numbers
        a, b = b, a + b
        fibonacci_numbers.append(b)
        cubes.append(b**3)

    return fibonacci_numbers, cubes