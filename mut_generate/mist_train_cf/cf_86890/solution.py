"""
QUESTION:
Create a function `find_twin_primes` that takes a list of integers as input. Implement a primality test from scratch, without using any built-in functions or libraries. The function should return a list of tuples, where each tuple contains a prime number from the original list and a boolean value indicating whether it is a twin prime (i.e., the number before or after it is also prime). Optimize the function to achieve a time complexity of O(n * log(log(m))), where n is the length of the input list and m is the largest number in the list.
"""

def find_twin_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in lst:
        primes.append((num, is_prime(num) and (is_prime(num-2) or is_prime(num+2))))
    return primes