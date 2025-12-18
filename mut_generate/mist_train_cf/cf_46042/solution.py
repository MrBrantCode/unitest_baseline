"""
QUESTION:
Write a function `prime_factors(n)` that takes an integer `n` as input and returns a list of its prime factors. The function should handle cases where `n` is a prime number greater than 2 and optimize the search space by only checking odd factors up to the square root of `n`.
"""

def prime_factors(n):
    # Initialize an empty list to hold our prime factors
    prime_factors = []

    # First get the number of two's that divide n
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    # n must be odd at this point, thus skip one element (Note i = i +2)
    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            prime_factors.append(int(i))
            n = n / i
             
    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        prime_factors.append(int(n))
        
    return prime_factors