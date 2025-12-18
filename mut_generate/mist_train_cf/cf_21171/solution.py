"""
QUESTION:
Write a function `sum_of_primes(n, m, x)` that takes three parameters: `n` as the number of prime numbers, `m` as the starting number, and `x` as the minimum value of prime numbers. The function should return the sum of the first `n` prime numbers greater than `x` starting with `m`. The prime numbers must be greater than `x`.
"""

def sum_of_primes(n, m, x):
    primes = []  # List to store the prime numbers
    num = m  # Start with m
    
    while len(primes) < n:
        is_prime = True
        
        # Check if num is a prime number
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        # If num is prime and greater than x, add it to the list of primes
        if is_prime and num > x:
            primes.append(num)
        
        num += 1  # Increment num for the next iteration
    
    return sum(primes)  # Return the sum of all prime numbers