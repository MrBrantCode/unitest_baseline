"""
QUESTION:
Create a Python program with two functions, `is_prime(n, divisor=2)` and `print_prime_numbers(count, number=2)`, that prints the first 'n' prime numbers. The `is_prime` function should use recursion to check if a number is prime, and the `print_prime_numbers` function should use recursion to print the prime numbers. The `print_prime_numbers` function should take an integer 'count' representing the number of prime numbers to print and an optional integer 'number' representing the current number to check for primality, defaulting to 2.
"""

def entrance(n, number=2):
    if n == 0:
        return
    if is_prime(number):
        print(number, end=' ')
        entrance(n - 1, number + 1)
    else:
        entrance(n, number + 1)

def is_prime(n, divisor=2):
    if n <= 2:
        return n == 2
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)