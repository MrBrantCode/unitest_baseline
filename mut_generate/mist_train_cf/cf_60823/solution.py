"""
QUESTION:
Create a function named `matrix_prime_sum(matrix)` that calculates the sum of all prime number elements in a given 2D matrix of integers. A prime number is defined as a natural number greater than 1 with no positive divisors other than 1 and itself. The matrix will only contain integers, and the function should return the total sum of prime numbers found in the matrix.
"""

def is_prime(n):
    """ Check if an integer is a prime number """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def matrix_prime_sum(matrix):
    """ Calculate the sum of the prime number elements in a matrix """
    prime_sum = 0
    for row in matrix:
        for element in row:
            if is_prime(element):
                prime_sum += element
    return prime_sum