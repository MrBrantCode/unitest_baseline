"""
QUESTION:
Write a function `find_primes_with_digit_sum(m, n)` that takes two positive integers `m` and `n` as input and returns a list of prime numbers between `m` and `n` (inclusive), along with the sum of their digits. The function should return a list of tuples, where each tuple contains a prime number and the sum of its digits.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_with_digit_sum(m, n):
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))
    
    primes_with_digit_sum = []
    for num in range(m, n + 1):
        if is_prime(num):
            primes_with_digit_sum.append((num, digit_sum(num)))
    return primes_with_digit_sum