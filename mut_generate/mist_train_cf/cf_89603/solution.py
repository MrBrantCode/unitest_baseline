"""
QUESTION:
Write a recursive function named `print_primes` that prints all prime numbers between a given start and end (inclusive) without using any loops or conditional statements. The function should utilize a helper function named `check_prime` to verify if a number is prime. The helper function should check if a number is prime by recursively dividing it by decreasing divisors. The `print_primes` function should call itself for the next number in the range after checking if the current number is prime.
"""

def print_primes(start, end):
    def check_prime(number, divisor):
        if divisor == 1:
            return True
        if number % divisor == 0:
            return False
        return check_prime(number, divisor - 1)

    if start <= end:
        if start > 1 and check_prime(start, start - 1):
            print(start)
        elif start == 1:
            print(1)
        print_primes(start + 1, end)

def check_prime(number, divisor):
    if divisor == 1:
        return True
    if number % divisor == 0:
        return False
    return check_prime(number, divisor - 1)