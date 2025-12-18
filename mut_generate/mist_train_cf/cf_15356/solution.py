"""
QUESTION:
Write a function named `find_square_of_primes` that takes a positive integer `n` as input. The function should find the square of the first `n` prime numbers, calculate the sum of the squares, and return both the sum and the list of squares as output.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_square_of_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    squares = [prime ** 2 for prime in primes]
    sum_of_squares = sum(squares)
    
    return sum_of_squares, squares