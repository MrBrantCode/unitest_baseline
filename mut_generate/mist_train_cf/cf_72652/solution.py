"""
QUESTION:
Write a function `circular_primes(limit)` that returns the number of circular primes below the given limit. A circular prime is a prime number with the property that the number generated at each intermediate step when cyclically permuting its (base 10) digits will be prime. For example, 1193 is a circular prime, since 1931, 9311 and 3119 all are also prime. The input limit is a positive integer and the output should be an integer representing the count of circular primes below the limit.
"""

def circular_primes(limit):
    def SieveOfEratosthenes(limit):
        sieve = [True]*limit
        sieve[0] = sieve[1] = False

        for start in range(2,int(limit**0.5)+1):
            if sieve[start]:
                for i in range(start*start, limit, start):
                    sieve[i]= False
                    
        primes = [x for x in range(2, limit) if sieve[x]]
        return primes

    def rotations(num):
        num = str(num)
        return [int(num[i:]+num[:i]) for i in range(len(num))]

    primes = SieveOfEratosthenes(limit)
    counter = 0
    for prime in primes:
        if all(x in primes for x in rotations(prime)):
            counter += 1
    return counter