"""
QUESTION:
Write a function `print_primes` that prints all prime numbers between a given start and end range without using any explicit loops or conditional statements (if statements). The function should be able to handle any range of integers.
"""

def print_primes(start, end):
    def check_prime(number, divisor):
        if divisor == 1:
            return True
        if number % divisor == 0:
            return False
        return check_prime(number, divisor - 1)

    if start <= end:
        is_prime = True
        if start > 1:
            is_prime = check_prime(start, start - 1)
        if is_prime and start > 1:
            print(start)
        print_primes(start + 1, end) if start < end else None