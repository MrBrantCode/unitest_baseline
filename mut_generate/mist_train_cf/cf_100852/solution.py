"""
QUESTION:
Create a function named `sum_prime_factors` that calculates the sum of prime factors for each number in a given list of integers. The function should use the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to the highest number in the input list. Then, for each number in the input list, find all its prime factors and add them together to get the total sum of prime factors. The function should return a list of these sums.
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