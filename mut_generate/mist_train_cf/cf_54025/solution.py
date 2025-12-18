"""
QUESTION:
Create a function `second_largest_prime` that takes an array of unique positive integers as input and returns the second largest prime number in the array. If there are less than two prime numbers in the array, the function should return `None`. Assume that the array only contains integers and that the largest prime number may appear only once.
"""

def second_largest_prime(arr):
    primes = [i for i in arr if is_prime(i)]
    primes.sort()
    if len(primes) < 2:
        return None
    else:
        return primes[-2]

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True