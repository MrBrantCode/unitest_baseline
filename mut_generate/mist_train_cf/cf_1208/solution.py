"""
QUESTION:
Write a function called `sum_of_evens_and_primes` that calculates the sum of all even numbers and the sum of all prime numbers between 1 and a given number `n`. The function should have a time complexity of O(n^2) and a space complexity of O(1). The function should return a tuple containing the sum of even numbers and the sum of prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_of_evens_and_primes(n):
    even_sum = 0
    prime_sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even_sum += i
        if is_prime(i):
            prime_sum += i
    return even_sum, prime_sum