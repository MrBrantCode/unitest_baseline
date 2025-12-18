"""
QUESTION:
Create a function `get_primes_between_1_and_n` that generates an array of prime numbers between 1 and a given number n. In this case, n is 10. The function should return the array of prime numbers.
"""

def get_primes_between_1_and_n(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes