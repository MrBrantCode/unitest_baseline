"""
QUESTION:
Implement a function named `print_primes_without_digit_5(start, end)` that takes two integers `start` and `end` as input and prints all prime numbers between `start` and `end` (inclusive) excluding any prime numbers that contain the digit 5. The function should be optimized to handle larger inputs efficiently.
"""

def contains_digit_5(n):
    while n > 0:
        if n % 10 == 5:
            return True
        n //= 10
    return False

def print_primes_without_digit_5(start, end):
    # Generating primes up to the largest number in the range
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= end:
        if sieve[p]:
            for i in range(p * p, end + 1, p):
                sieve[i] = False
        p += 1
    
    # Printing the primes without digit 5
    for i in range(start, end + 1):
        if sieve[i] and not contains_digit_5(i):
            print(i)