"""
QUESTION:
Generate a function `generate_primes(n)` that returns a list of all prime numbers from 1 to n, excluding multiples of 3. The function should have a time complexity of O(n) and the output list should not be considered when calculating the space complexity.
"""

def generate_primes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            if i % 3 != 0:  
                for j in range(i*i, n+1, i):
                    primes[j] = False

    prime_list = []
    for i in range(2, n+1):
        if primes[i] and i % 3 != 0:  
            prime_list.append(i)

    return prime_list