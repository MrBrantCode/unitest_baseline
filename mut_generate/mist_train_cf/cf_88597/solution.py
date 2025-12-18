"""
QUESTION:
Write a function called `sum_of_primes` that calculates the total of all the prime numbers in a given list. The list may contain up to 1000 elements and the function must use a loop to check for prime numbers without using any built-in functions or libraries.
"""

def sum_of_primes(numbers):
    def is_prime(num):
        if num < 2:  
            return False
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in numbers:
        if is_prime(num):
            prime_sum += num
    return prime_sum