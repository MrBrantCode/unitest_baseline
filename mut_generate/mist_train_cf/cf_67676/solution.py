"""
QUESTION:
Create a function named `primes_between` that takes two parameters: `start` and `end`, representing the start and end points of a range. The function should return a list of distinct prime numbers within this range. The function should only consider numbers greater than or equal to 2 and less than or equal to `end`. It should also optimize the prime check by only checking divisibility for numbers up to the square root of the possible prime.
"""

def primes_between(start, end):
    primes = []
    for possiblePrime in range(max(2,start), end + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes