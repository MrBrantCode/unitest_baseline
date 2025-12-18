"""
QUESTION:
Implement the function `sum_odd_primes` that recursively calculates the sum of all odd values in a given 2D list where the column index is a prime number, without modifying the original data structure. The function should take a 2D list as input and return the calculated sum.
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

def sum_odd_primes(data, row=0, col=0):
    if row >= len(data):
        return 0
    if col >= len(data[row]):
        return sum_odd_primes(data, row+1, 0)
    value = data[row][col]
    if value % 2 == 1 and is_prime(col):
        return value + sum_odd_primes(data, row, col+1)
    return sum_odd_primes(data, row, col+1)