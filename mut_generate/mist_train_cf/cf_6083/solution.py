"""
QUESTION:
Write a function called `find_primes` that takes a positive integer `n` as input and returns the total count of prime numbers and the sum of all prime numbers between 1 and `n`. The function should not use any built-in libraries or functions for prime number calculation or checking, and its time complexity should be O(n*sqrt(n)).
"""

def find_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    total_sum = 0
    for num in range(2, n+1):
        if is_prime(num):
            count += 1
            total_sum += num
    return count, total_sum