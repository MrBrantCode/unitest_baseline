"""
QUESTION:
Create a function `print_primes_desc(arr)` that takes an array of integers as input and prints all the prime numbers in descending order.
"""

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to print prime numbers in descending order
def print_primes_desc(arr):
    primes = [num for num in arr if is_prime(num)]
    primes.sort(reverse=True)
    for prime in primes:
        print(prime)