"""
QUESTION:
Write a function named `sum_of_primes` that takes no arguments. The function should calculate the sum of all prime numbers between 1000 and 1100 (inclusive) that are not palindromes. A palindrome is a number that remains the same when its digits are reversed. The function should return the calculated sum.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes():
    prime_sum = 0
    for num in range(1000, 1101):
        if is_prime(num) and str(num) != str(num)[::-1]:
            prime_sum += num
    return prime_sum