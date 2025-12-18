"""
QUESTION:
Create a function named `sum_of_cubes` that takes a single argument `n`, a positive integer. The function should return the sum of all cubes from 1 to `n` and also print the cube of each number before adding it to the sum.
"""

def sum_of_cubes(n):
    sum = 0
    for i in range(1, n+1):
        cube = i**3
        sum += cube
        print(f"The cube of {i} is {cube}")
    return sum