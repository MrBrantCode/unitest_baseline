"""
QUESTION:
Write a function `print_primes(n)` that prints all prime numbers from 1 to n, separated by a semicolon. The function should not take any input other than the integer n and should print the output directly without returning a value. The prime numbers should be printed in ascending order.
"""

def print_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    i = 2
    while i <= n:
        if is_prime(i):
            print(i, end=";")
        i += 1