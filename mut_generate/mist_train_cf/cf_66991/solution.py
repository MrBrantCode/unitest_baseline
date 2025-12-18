"""
QUESTION:
Write a function named `steins_algorithm` that takes two positive integers greater than 1 as input and returns their greatest common factor using Stein's algorithm, along with the steps of the calculation process.
"""

def steins_algorithm(x, y):
    if x == y:
        return x

    # Make x the larger number
    if x < y:
        x, y = y, x

    if x == 0:
        return y

    # Remove common factor of 2
    if x % 2 == 0 and y % 2 == 0:
        return 2 * steins_algorithm(x // 2, y // 2)

    # If x is even, divide by 2
    if x % 2 == 0:
        return steins_algorithm(x // 2, y)

    # If y is even, divide by 2
    if y % 2 == 0:
        return steins_algorithm(x, y // 2)

    # Subtract the smaller number given both are odd
    return steins_algorithm((x-y) // 2, y)