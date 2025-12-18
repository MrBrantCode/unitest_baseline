"""
QUESTION:
Write a function `classify_numbers` that accepts a list of integers and returns two lists: one for prime numbers and one for composite numbers. The function should not include 1 as a prime number and should efficiently handle large numbers by checking up to the square root of each number.
"""

def classify_numbers(numbers):
    primes = []
    composites = []
    
    for n in numbers:
        if n < 2: 
            continue
        for i in range(2, int(n ** 0.5) + 1): 
            if n % i == 0:
                composites.append(n)
                break
        else:
            primes.append(n)
    
    return primes, composites