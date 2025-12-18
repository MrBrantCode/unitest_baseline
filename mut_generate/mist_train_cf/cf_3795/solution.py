"""
QUESTION:
Write a function `sum_of_primes(n)` to find the sum of all prime numbers between 0 and n (inclusive), where n is a positive integer. The function should have a time complexity of O(n log(log n)).
"""

def sum_of_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    
    for p in range(2, int(n**0.5)+1):
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
    
    return sum(p for p in range(2, n+1) if is_prime[p])