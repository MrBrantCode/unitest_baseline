"""
QUESTION:
Write a function named `categorize_numbers` that takes an input of either a single integer or a list of integers and categorizes them into prime, composite, and not valid numbers. The function should handle edge cases and exceptional inputs without crashing and provide suitable error messages to the user. The categorization should be based on the definition that a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers, and a composite number is a natural number greater than 1 that is not prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

def categorize_numbers(numbers):
    primes = []
    composites = []
    not_valid = []
    
    for num in numbers:
        if type(num) != int or num < 0:
            not_valid.append(num)
        elif is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
            
    return primes, composites, not_valid