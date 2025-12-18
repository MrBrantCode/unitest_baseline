"""
QUESTION:
Write a function named `prime_and_factors` that takes a positive integer `num` as input and returns a dictionary where the keys are the factors of `num` and the corresponding values are boolean values indicating whether each factor is a prime number or not.
"""

def prime_and_factors(num):
    def is_prime(n):
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
    
    result = {}
    for i in range(1, num+1):
        if num % i == 0:
            result[i] = is_prime(i)
    return result