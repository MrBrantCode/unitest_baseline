"""
QUESTION:
Create a function `print_divisible(matrix, prime)` that takes a 2D array `matrix` containing floating point numbers with up to 2 decimal places and a prime number `prime` as input. The function should print the elements of the matrix that are divisible by the provided prime number, where the prime number is between 2 and 19.
"""

def print_divisible(matrix, prime):
    # Check if the provided number is valid (prime and in the accepted range)
    if prime not in [2, 3, 5, 7, 11, 13, 17, 19]:
        return 'The number provided is not a prime number between 2 and 19'

    # Traverse and print the divisible elements
    for row in matrix:
        for num in row:
            # Check if the number is divisible by the provided prime
            if round(num, 2) % prime == 0:
                print(num)