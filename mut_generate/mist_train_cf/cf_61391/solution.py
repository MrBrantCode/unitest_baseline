"""
QUESTION:
Create a function called `generate_matrix(n, order)` that takes two parameters: an integer `n` and a string `order`. The function should return a square matrix of dimension `n`x`n` filled with numbers ranging from 1 to `n` squared if `n` is less than or equal to 10, and with prime numbers if `n` is greater than 10. The matrix should be filled in either row-major or column-major order, depending on the value of the `order` parameter, which must be either 'row-major' or 'column-major'.
"""

import numpy

def is_prime(n):
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

def generate_primes(n):
    primes = []
    i = 1
    while len(primes) < n*n:
        i += 1
        if is_prime(i): primes.append(i)
    return primes

def generate_matrix(n, order):
    if order not in ['row-major', 'column-major']:
        print('Invalid order! Please choose "row-major" or "column-major".')
        return None

    if n > 10:
        numbers = generate_primes(n)
    else:
        numbers = list(range(1, n*n+1))

    matrix = numpy.zeros((n, n))

    if order == 'row-major':
        for i, x in enumerate(numbers):
            matrix[i//n, i%n] = x
    elif order == 'column-major':
        for i, x in enumerate(numbers):
            matrix[i%n, i//n] = x
    return matrix