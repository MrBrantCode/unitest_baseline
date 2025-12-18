"""
QUESTION:
Write a function `find_prime_numbers(n)` that generates and returns the first n prime numbers without using any built-in functions or libraries to check for prime numbers. The input `n` is a positive integer, and the function should be efficient in finding prime numbers.
"""

def find_prime_numbers(n):
    primes = []
    is_prime = [True] * (n*10+1)  

    for number in range(2, n*10+1):
        if is_prime[number]:
            primes.append(number)  

            for multiple in range(number*2, n*10+1, number):
                is_prime[multiple] = False

        if len(primes) == n:
            break

    return primes