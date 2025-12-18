"""
QUESTION:
Create a function named `find_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should have a time complexity of O(n^2), where n is the length of the input list.
"""

def find_prime_numbers(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    
    return primes