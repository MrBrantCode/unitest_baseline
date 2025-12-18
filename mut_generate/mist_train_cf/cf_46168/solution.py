"""
QUESTION:
Write a function named `count_primes` that takes a one-dimensional list of integers as a parameter and returns the number of prime numbers in the list.
"""

def count_primes(l):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    count = 0
    for elem in l:
        if is_prime(elem):
            count += 1
    return count