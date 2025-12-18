"""
QUESTION:
Write a function called `next_divisible(n)` that takes a positive integer `n` as input and returns the next number which is divisible by both 7 and the smallest prime factor of `n`, excluding 2. If `n` is already divisible by both 7 and its smallest prime factor, the function should return `n`.
"""

def smallest_prime(n):
    if n % 2 == 0:
        n += 1 #if number is even, increment by 1 to start with an odd number

    # divide n by all numbers up to sqrt(n) and see if any divides evenly
    for x in range(3, int(n**0.5) + 1, 2): 
        if n % x == 0:
            return x
    return n

def next_divisible(n):
    sp = smallest_prime(n)

    # if n is already divisible by both sp and 7, return it
    if n % sp == 0 and n % 7 == 0:
        return n

    # Otherwise keep incrementing n by 1 until we find a number that is
    while n % sp != 0 or n % 7 != 0:
        n += 1

    return n