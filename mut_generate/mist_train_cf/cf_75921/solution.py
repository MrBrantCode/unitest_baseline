"""
QUESTION:
Write a function `is_prime_palindrome(numbers)` that takes a list of numbers as input. The function should identify the prime numbers in the list, split them into two separate lists (prime palindromes and non-palindrome primes), and return the sum of each list. A prime number is a natural number greater than 1 with no positive divisors other than 1 and itself. A palindrome is a number that reads the same forwards and backwards. Do not use any additional libraries besides the math library.
"""

import math

def is_prime_palindrome(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    primes = [n for n in numbers if is_prime(n)]
    prime_palindromes = [n for n in primes if is_palindrome(n)]
    other_primes = [n for n in primes if not is_palindrome(n)]
    
    return sum(prime_palindromes), sum(other_primes)