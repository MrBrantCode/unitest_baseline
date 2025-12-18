"""
QUESTION:
Create a function named `find_primes` that uses list comprehension to return all prime numbers from a given list of integers. The function should optimize the prime number check by only considering divisors up to the square root of each number.
"""

def find_primes(numbers):
    return [num for num in numbers if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1))]