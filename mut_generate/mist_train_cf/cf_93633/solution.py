"""
QUESTION:
Write a function `count_unique_primes` that takes a list of integers as input and returns the count of unique prime numbers in the list. The function should have a time complexity of O(n), where n is the length of the list, and should not use any built-in functions or libraries to check for prime numbers.
"""

def count_unique_primes(my_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    unique_primes = set()
    for num in my_list:
        if is_prime(num):
            unique_primes.add(num)
    return len(unique_primes)