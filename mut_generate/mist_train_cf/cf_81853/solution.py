"""
QUESTION:
Write a function named `spiral_diagonals_sum` that calculates the sum of the numbers on the diagonals in a spiral formed by moving in a counter-clockwise direction, starting from the number 1, and filling in a square grid of size n by n. The function should only take one argument, `n`, which represents the size of the grid. The grid size is guaranteed to be an odd number greater than 1.
"""

def spiral_diagonals_sum(n):
    total = 1
    for i in range(3, n+1, 2):
        total += 4*i**2 - 6*i + 6
    return total