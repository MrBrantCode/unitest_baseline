"""
QUESTION:
Write a function `sieve_of_eratosthenes(limit)` that finds all prime numbers from 0 to a given limit, returns them in sorted order, and optimizes for efficiency and minimizes memory usage. The function should take an integer `limit` as input and return a list of prime numbers.
"""

def sieve_of_eratosthenes(limit):
    # Create a boolean array "prime[0..limit]" and initialize all entries as True.
    # A value in prime[i] will finally be False if i is not a prime, else True.
    prime = [True] * (limit+1)
    
    # 0 and 1 are not prime numbers, so we set their flags to False.
    prime[0] = prime[1] = False
    
    p = 2  # Start with the first prime number
    
    while p * p <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, limit+1, p):
                prime[i] = False
        p += 1
    
    # Return a list of all prime numbers
    primes = [num for num, is_prime in enumerate(prime) if is_prime]
    
    return primes