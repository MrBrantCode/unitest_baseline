"""
QUESTION:
Create a function `sieve_of_atkin` that generates a list of all prime numbers up to a given limit using the Sieve of Atkin algorithm. The function should take an integer `limit` as input and return a list of prime numbers. The function should be able to handle large inputs efficiently.
"""

def sieve_of_atkin(limit):
    # Initialize the sieve
    sieve = [False] * (limit + 1)

    # Set up the basic prime numbers
    sieve[2] = True
    sieve[3] = True

    # Mark sieve[i] is True if one of the following is True:
    # a) i = (4*x*x)+(y*y) has odd number of solutions, i.e., there exist odd number of distinct pairs (x, y)
    #    that satisfy the equation and i % 12 = 1 or i % 12 = 5.
    # b) i = (3*x*x)+(y*y) has odd number of solutions
    #    and i % 12 = 7
    # c) i = (3*x*x)-(y*y) has odd number of solutions, x > y and i % 12 = 11
    for x in range(1, int(limit ** 0.5) + 1):
        for y in range(1, int(limit ** 0.5) + 1):
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    # Mark all multiples of squares as non-prime
    for r in range(5, int(limit ** 0.5) + 1):
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False

    # Add primes to the results list
    results = [i for i in range(5, limit + 1) if sieve[i]]
    results.insert(0, 2)
    results.insert(1, 3)
    return results