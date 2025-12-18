"""
QUESTION:
Create a function named `sum_prime_factors` that takes a list of integers as input and returns a list where each element at index i is the sum of prime factors of the input number at index i. Use the Sieve of Eratosthenes algorithm to generate prime numbers up to the maximum number in the input list.
"""

def sum_prime_factors(numbers):
    # Find the highest number in the input list
    max_number = max(numbers)
    
    # Generate a list of prime numbers up to the highest number
    primes = []
    sieve = [True] * (max_number + 1)
    for i in range(2, max_number + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, max_number + 1, i):
                sieve[j] = False
    
    # Calculate the sum of prime factors for each number in the input list
    result = []
    for num in numbers:
        sum_factors = 0
        for prime in primes:
            if prime > num:
                break
            while num % prime == 0:
                sum_factors += prime
                num /= prime
        result.append(sum_factors)
    return result