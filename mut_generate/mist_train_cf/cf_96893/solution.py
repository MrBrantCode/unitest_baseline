"""
QUESTION:
Create a function `generate_prime_numbers(n)` that generates a list of all the prime numbers in the range from 0 to the given number `n`, excluding any prime numbers that contain the digit 5. The function should have a time complexity of O(n log(log n)).
"""

def generate_prime_numbers(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    p = 2
    while p * p <= n:
        if isPrime[p]:
            if '5' in str(p):
                isPrime[p] = False
            else:
                for i in range(p * p, n + 1, p):
                    isPrime[i] = False
        p += 1

    primes = []
    for i in range(n + 1):
        if isPrime[i] and '5' not in str(i):
            primes.append(i)

    return primes