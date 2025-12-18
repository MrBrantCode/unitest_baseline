"""
QUESTION:
Create a function called `find_twin_primes` that takes a list of integers as input and returns a list of tuples. Each tuple should contain a prime number from the input list and a boolean value indicating whether the prime number is a twin prime or not. A twin prime is a prime number that is either 2 less or 2 more than another prime number. Do not use any built-in functions or libraries for prime number calculation and implement the primality test yourself. The function should have a time complexity of O(n * log(log(m))), where n is the length of the input list and m is the largest number in the list.
"""

def find_twin_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_twin_prime(n):
        if is_prime(n) and (is_prime(n-2) or is_prime(n+2)):
            return True
        return False

    primes = []
    for num in lst:
        if is_prime(num):
            primes.append((num, is_twin_prime(num)))
    return primes