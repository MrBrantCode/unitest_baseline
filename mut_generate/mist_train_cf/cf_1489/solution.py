"""
QUESTION:
Write a function called `sum_of_palindrome_primes` that calculates the sum of the first 100 prime numbers that are also palindromes. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A palindrome is a number that remains the same when its digits are reversed. Do not use any external modules other than the built-in math module.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def sum_of_palindrome_primes():
    limit = 100
    count = 0
    prime_sum = 0
    num = 2
    
    while count < limit:
        if is_prime(num) and is_palindrome(num):
            prime_sum += num
            count += 1
        num += 1
    
    return prime_sum