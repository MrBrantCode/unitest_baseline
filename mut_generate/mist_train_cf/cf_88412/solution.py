"""
QUESTION:
Write a function `find_primes(numbers)` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should not use any built-in functions or libraries to check if a number is prime and should be optimized to find the prime numbers in the most efficient way possible. The function should handle edge cases where the input list is empty or contains negative numbers.
"""

def find_primes(numbers):
    if not numbers or min(numbers) < 0:
        return []

    # Find the maximum number in the list
    max_num = max(numbers)

    # Create a list of booleans, initially assuming all numbers are prime
    is_prime = [True] * (max_num + 1)

    # Set 0 and 1 as non-prime
    is_prime[0] = is_prime[1] = False

    # Iterate from 2 to sqrt(max_num) and mark multiples as non-prime
    i = 2
    while i * i <= max_num:
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
        i += 1

    # Generate a new list with only prime numbers
    primes = [num for num in numbers if is_prime[num]]
    return primes