"""
QUESTION:
Write a function called `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list and the list of these prime numbers. If no prime numbers are found, return the message "No prime numbers found".
"""

def sum_of_primes(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    primes = [i for i in lst if is_prime(i)]
    if len(primes) == 0:
        return "No prime numbers found"
    else:
        return "Sum of all prime numbers: " + str(sum(primes)) + "\nList of prime numbers: " + str(primes)