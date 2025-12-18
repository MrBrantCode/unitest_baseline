"""
QUESTION:
Create a function `print_primes(n)` to print all prime numbers up to `n` using a recursive approach. The function should exclude prime numbers that are palindromic and contain only odd digits.
"""

def is_prime(num, divisor=2):
    if num <= 2:
        return num == 2
    if num % divisor == 0:
        return False
    if divisor * divisor > num:
        return True
    return is_prime(num, divisor + 1)

def is_palindromic_odd(number):
    if number < 10:
        return number % 2 != 0
    return number % 2 != 0 and number % 10 % 2 != 0 and number // 10 % 10 % 2 != 0 and is_palindromic_odd(number // 10)

def print_primes(n, current=2):
    if current <= n:
        if not is_palindromic_odd(current) and is_prime(current):
            print(current)
        print_primes(n, current + 1)