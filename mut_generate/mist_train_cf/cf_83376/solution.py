"""
QUESTION:
Write a function `primeFactors(n)` that takes an integer `n` as input and returns a list of its prime factors. The function should have a time complexity of approximately O(sqrt(n)) and should be able to handle large inputs. The function should only consider prime numbers as potential factors, and it should return the prime factors in any order.
"""

def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
        if i == 2:  
            i += 1
    if n > 1:
        factors.append(n)
    return factors