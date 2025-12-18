"""
QUESTION:
Create a function `is_prime(n)` that checks if a given number `n` is prime, with a time complexity of O(n/log(log(n))). The function should return `True` if the number is prime and `False` otherwise.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False
    
    for p in range(3, int(n ** 0.5) + 1, 2):
        if isPrime[p]:
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
    
    return isPrime[n]