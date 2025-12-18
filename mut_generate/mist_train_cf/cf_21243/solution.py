"""
QUESTION:
Write a function called "search_prime_numbers" that takes a positive integer "n" as a parameter and prints all prime numbers up to and including "n". Implement the Sieve of Eratosthenes algorithm to generate prime numbers efficiently. The function should optimize the process to reduce unnecessary calculations by only checking divisibility up to the square root of each number.
"""

def search_prime_numbers(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]