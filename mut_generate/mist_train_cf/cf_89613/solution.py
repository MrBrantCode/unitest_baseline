"""
QUESTION:
Create a recursive function `print_prime_numbers` that prints the first 'n' prime numbers, where 'n' is a positive integer. The function should check for primality using another recursive function `is_prime` that takes two parameters: a number to check for primality and an optional divisor starting from 2. The `is_prime` function should return True if the number is prime and False otherwise. The `print_prime_numbers` function should print the prime numbers separated by a space.
"""

def is_prime(n, divisor=2):
    if n <= 2:
        return n == 2
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)

def print_prime_numbers(count, number=2):
    if count == 0:
        return
    if is_prime(number):
        print(number, end=' ')
        print_prime_numbers(count - 1, number + 1)
    else:
        print_prime_numbers(count, number + 1)