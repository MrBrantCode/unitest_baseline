"""
QUESTION:
Create a function `sum_of_primes(arr)` that takes a two-dimensional array of integers as input and returns the sum of all prime numbers in the array. The function should handle arrays with any number of sublists and any number of elements in each sublist. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(arr):
    # Iterate through each element in the array and add primes to the sum
    prime_sum = 0
    for sublist in arr:
        for num in sublist:
            if is_prime(num):
                prime_sum += num
    return prime_sum