"""
QUESTION:
Write a function `prime_numbers(n)` that generates a list of all prime numbers between 2 and N (inclusive). Ensure the function is fault-tolerant by adding error handling for non-positive integers and non-integer inputs. The function should be optimized to reduce the number of iterations for identifying primes, and it should handle values of N up to 10^5.
"""

def prime_numbers(n):
    try:
        n = int(n)
    except ValueError:
        return "Error: Input is not an integer."

    if n < 2:
        return "Error: Input should be a positive integer greater or equal to 2."

    primes = [True for _ in range(n+1)]
    p = 2
    while(p * p <= n):
        if primes[p] == True: 
            for i in range(p * p, n+1, p): 
                primes[i] = False
        p += 1  

    prime_numbers = [p for p in range(2, n+1) if primes[p]]
    return prime_numbers