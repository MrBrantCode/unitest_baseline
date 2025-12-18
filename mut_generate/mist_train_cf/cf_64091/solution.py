"""
QUESTION:
Create a function `filter_strings_with_primes` that takes an array of strings as input and returns a new array containing only the strings that include a prime number in their text. The function should be able to identify prime numbers up to at least 4 digits.
"""

def seive_of_era(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p**2 <= n):
        if prime[p] == True:
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

def filter_strings_with_primes(arr):
    primes = seive_of_era(10000)  # consider n up to 10000
    return [string for string in arr if any(str(prime) in string for prime in primes)]