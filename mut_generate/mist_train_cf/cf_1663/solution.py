"""
QUESTION:
Declare a variable "x" to store the sum of the first 20 prime numbers. The sum should be calculated by identifying the first 20 prime numbers and adding them together. What is the suitable data type for "x"?
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return sum(primes)