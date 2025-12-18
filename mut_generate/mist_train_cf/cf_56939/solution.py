"""
QUESTION:
Design a function named `primefactors(n)` that takes an integer `n` as input and returns a dictionary containing its prime factors as keys and their respective powers as values. Additionally, create a helper function `isprime(n)` to check if a number is prime in O(sqrt(n)) time. The `primefactors(n)` function should also have a time complexity of O(sqrt(n)) and should handle cases where `n` is a prime number greater than 2.
"""

import math

# Helper function to check if a number is prime in O(sqrt(n)) time.
def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find the prime factors of a number.
def primefactors(n):
    factors={}
    count = 0
    # Count the number of 2s that divide n
    while n % 2 == 0:
        n /= 2
        count += 1
    if count > 0:
        factors[2] = count

    # n is now odd, we can skip the even numbers.
    for i in range(3,int(math.sqrt(n))+1,2):
        count = 0
        while n % i== 0:
            n /= i
            count += 1
        if count > 0:
            factors[i] = count

    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        factors[n] = 1

    return factors