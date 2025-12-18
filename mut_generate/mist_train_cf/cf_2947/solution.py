"""
QUESTION:
Implement a function called `contains_three_odd_primes` that takes an array of integers as input and returns `True` if the array contains at least three odd prime numbers whose sum is also a prime number, and `False` otherwise.
"""

def contains_three_odd_primes(array):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    odd_primes = []
    for num in array:
        if num % 2 != 0 and is_prime(num):
            odd_primes.append(num)
        if len(odd_primes) == 3:
            break
    
    if len(odd_primes) < 3:
        return False
    
    sum_odd_primes = sum(odd_primes)
    if is_prime(sum_odd_primes):
        return True
    return False