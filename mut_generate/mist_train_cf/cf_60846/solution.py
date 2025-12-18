"""
QUESTION:
Create a function named `find_primes_in_range` that takes two parameters `C` and `D` representing an inclusive range. Using recursive calls, this function should find all prime numbers within this range and print 'single prime' if there's only one prime number, or 'multiple primes' if there are more than one prime number in the range. The function should return the list of prime numbers found. Optimize the function to handle large ranges efficiently.
"""

def find_primes_in_range(C, D):
    def sieve_of_eratosthenes(n):
        primes = [True for i in range(n+1)]
        p = 2
        while (p**2 <= n):
            if primes[p] == True:
                for i in range(p**2, n+1, p):
                    primes[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n) if primes[p]]
        return prime_numbers

    primes = sieve_of_eratosthenes(D)
    primes_in_range = [i for i in primes if i >= C]
    if len(primes_in_range) > 1:
        print('multiple primes')
    elif len(primes_in_range) == 1:
        print('single prime')
    return primes_in_range