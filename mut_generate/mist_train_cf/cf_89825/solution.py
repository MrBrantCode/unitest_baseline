"""
QUESTION:
Write a function that prints a list of all prime numbers from 0 to 10,000. The solution should use an optimized algorithm with a time complexity of O(n log(log n)) or better and avoid using built-in functions or libraries that directly solve the problem. The function should be implemented in Python.
"""

def print_primes_up_to_n(n):
    primes = []
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: 
            for i in range(x*x, n+1, x): 
                sieve[i] = False
    for x in range(2, n):
        if sieve[x]: 
            primes.append(x)
    return primes

def entrance():
    n = 10000
    primes = print_primes_up_to_n(n)
    for i in primes:
        print(i)

# removing entrance call to avoid unnecessary output
# entrance()