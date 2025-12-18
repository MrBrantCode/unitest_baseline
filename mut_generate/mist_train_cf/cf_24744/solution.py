"""
QUESTION:
Create a function named `list_primes` that takes two integer parameters, `start` and `end`, and returns a list of all prime numbers between `start` and `end` (inclusive). The function should not take any other parameters and should not use any external libraries.
"""

def list_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes