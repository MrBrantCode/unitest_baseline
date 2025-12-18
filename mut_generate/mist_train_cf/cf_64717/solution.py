"""
QUESTION:
Write a recursive function called `print_square` that takes an integer `n` as input and prints the square of each number from 1 to `n` without using loops. The function should also append an asterisk to the square if the number is prime. The function should handle the edge case where `n` is less than 1 and ensure efficiency in its algorithm.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_square(n):
    """
    Prints the square of each number from 1 to n without using loops.
    Appends an asterisk to the square if the number is prime.

    Args:
        n (int): The upper limit for printing squares.

    Returns:
        None
    """
    if n < 1: # edge case
        return
    print_square(n - 1)
    square = n * n
    if is_prime(n):
        print(str(square) + '*')
    else:
        print(str(square))