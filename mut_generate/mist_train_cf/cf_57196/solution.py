"""
QUESTION:
Write a function `check_for_prime` that takes a list of integers as input and returns a list of prime numbers in descending order. The function should not use any built-in functions or libraries for prime number identification. The input list may contain duplicates and the function should only return unique prime numbers. 

The input list can contain any integer, but the function should only consider integers greater than or equal to 2. The function should have a time complexity of O(n*sqrt(n)).
"""

def check_for_prime(numbers):
    def is_prime(n):
        if n < 2: 
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes = set(num for num in numbers if is_prime(num))
    return sorted(list(primes), reverse=True)