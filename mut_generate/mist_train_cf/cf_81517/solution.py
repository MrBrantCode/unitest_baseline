"""
QUESTION:
Create a function named `isPrime` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. However, if the input is not a valid integer (i.e., negative number, non-integer, or less than or equal to 1), the function should return `None`.

Create another function named `primeFactors` that identifies the smallest and the second smallest prime factors of a given number `n`. If `n` is a prime number, the function should identify it as such by returning a result that clearly indicates this. If the input is not a valid integer, the function should return `None`. The functions should be optimized to efficiently handle large numbers.
"""

def isPrime(n):
    if n <= 1 or (n % 1 > 0):
        return None
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

def primeFactors(n):
    if n <= 1 or (n % 1 > 0):
        return None

    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    i = 3
    while i*i <= n:
        while (n % i == 0):
            factors.append(i)
            n = n / i
        i += 2

    if n > 2:
        factors.append(n)

    return factors[:2]