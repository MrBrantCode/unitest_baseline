"""
QUESTION:
Write a function `is_prime` to check if a number is prime, and another function that finds and returns the sum of all odd prime numbers between 1 and 100 using a for-loop. The function should only consider odd numbers in the calculation of the sum.
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_odd_primes_sum():
    sum_of_odd_primes = 0
    for num in range(3, 101, 2):  # Iterating through odd numbers between 1 and 100
        if is_prime(num):
            sum_of_odd_primes += num
    return sum_of_odd_primes