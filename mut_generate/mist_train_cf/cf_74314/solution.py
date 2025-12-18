"""
QUESTION:
Create a function `descending_cubes` that takes a list of integers as input and returns a list containing the cubes of these integers in descending order. The function should use a helper function `cube` to calculate the cube of each integer using recursion. The list may contain any integers (positive, negative, or zero).
"""

def descending_cubes(numbers: list):
    """Return a list of cubed values in descending order
    """
    def cube(n):
        """Calculate cube of the number using recursion
        """
        if n == 1 or n == 0 or n == -1:
            return n
        else:
            return n * n * n

    # Cube each number in the list
    cubes = [cube(n) for n in numbers]

    # Sort in descending order
    cubes.sort(reverse=True)

    return cubes