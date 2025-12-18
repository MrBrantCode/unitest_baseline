"""
QUESTION:
Write a function `get_primes(start, end)` that generates a list of prime numbers between `start` and `end` (inclusive). A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient by only checking for divisors up to the square root of the number.
"""

def get_primes(start, end):
    """
    Generates a list of prime numbers between start and end (inclusive).
    
    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).
    
    Returns:
        list: A list of prime numbers between start and end.
    """
    primes = []
    for possiblePrime in range(start, end + 1):
        if possiblePrime > 1:
            isPrime = True
            for num in range(2, int(possiblePrime ** 0.5) + 1):
                if possiblePrime % num == 0:
                    isPrime = False
            if isPrime:
                primes.append(possiblePrime)
    return primes