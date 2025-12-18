"""
QUESTION:
Write a function named `prime_numbers` that takes an integer `n` as input and returns three values: a boolean indicating whether `n` is a prime number, the smallest prime number greater than `n`, and the sum of all prime numbers smaller than `n`. A prime number is an integer greater than 1 which is not divisible by any other numbers, except for 1 and itself. The function should handle integers greater than 1.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    is_prime_number = is_prime(n)
    smallest_prime = n + 1
    sum_of_primes = 0
    while True:
        if is_prime(smallest_prime):
            break
        smallest_prime += 1
    for i in range(2, n):
        if is_prime(i):
            sum_of_primes += i
    return is_prime_number, smallest_prime, sum_of_primes