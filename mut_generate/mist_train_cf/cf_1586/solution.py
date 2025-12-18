"""
QUESTION:
Write a function called `first_n_prime_palindromes` that generates the first n prime numbers that are also palindromes and their prime factors. The function should return a list of tuples where each tuple contains a prime palindrome and its corresponding prime factors. 

Note that a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself, and a palindrome is a number that remains the same when its digits are reversed. The prime factors of a number are the prime numbers that divide the number evenly. The input n should be a positive integer, and the function should stop generating prime palindromes once it has found n such numbers.
"""

import math

def first_n_prime_palindromes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def prime_factors(num):
        factors = []
        i = 2
        while i <= num:
            if num % i == 0:
                factors.append(i)
                num //= i
            else:
                i += 1
        return factors

    count = 0
    num = 2
    result = []

    while count < n:
        if is_prime(num) and is_palindrome(num):
            factors = prime_factors(num)
            result.append((num, factors))
            count += 1
        num += 1
    return result