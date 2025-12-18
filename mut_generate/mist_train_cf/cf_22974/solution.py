"""
QUESTION:
Create a function called `prime_factors(n)` that takes a positive integer `n` as input and returns a list of all prime factors excluding `n` itself, along with the count of prime factors, the sum of all prime factors, and the product of all prime factors. The function should handle inputs efficiently for large numbers.
"""

def prime_factors(n):
    factors = []
    count = 0
    total = 0
    product = 1
    
    # Check if 2 is a factor
    while n % 2 == 0:
        factors.append(2)
        count += 1
        total += 2
        product *= 2
        n //= 2

    # Check for other odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            count += 1
            total += i
            product *= i
            n //= i
        i += 2

    # If n is still greater than 2, it must be a prime factor
    if n > 2:
        factors.append(n)
        count += 1
        total += n
        product *= n
    
    # exclude n from factors
    if n == product:
        factors.pop()
        count -= 1
        total -= n
        product //= n
    
    return factors, count, total, product