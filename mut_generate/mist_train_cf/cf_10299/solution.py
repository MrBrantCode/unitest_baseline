"""
QUESTION:
Generate a function called `get_primes` that returns a list of all prime numbers within a given range (1 to n) in descending order. The function should only take one parameter, n, which is an integer representing the upper limit of the range.
"""

def get_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return sorted(primes, reverse=True)