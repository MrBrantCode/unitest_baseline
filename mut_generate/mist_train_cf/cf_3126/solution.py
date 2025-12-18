"""
QUESTION:
Create a function that prints a countdown from 100 to 1, displaying only the odd numbers that are also prime and calculate the sum of these prime numbers. The function should utilize a helper function to check for primality.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def countdown_and_sum_primes():
    sum_primes = 0
    for num in range(100, 0, -1):
        if num % 2 == 1 and is_prime(num):
            print(num)
            sum_primes += num
    print("Sum of prime numbers:", sum_primes)