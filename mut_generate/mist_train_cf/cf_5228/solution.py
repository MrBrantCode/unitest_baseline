"""
QUESTION:
Write a function named `calculate_prime_stats` that takes a list of prime numbers as input, calculates the sum of the prime numbers, finds the largest and smallest prime numbers, and returns their sum, largest number, smallest number, and the prime numbers in descending order. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def calculate_prime_stats(prime_numbers):
    """
    This function calculates the sum of the prime numbers, finds the largest and smallest prime numbers, 
    and returns their sum, largest number, smallest number, and the prime numbers in descending order.

    Args:
        prime_numbers (list): A list of prime numbers.

    Returns:
        tuple: A tuple containing the sum of prime numbers, the largest prime number, 
               the smallest prime number, and the prime numbers in descending order.
    """
    
    # Initialize variables
    sum_of_primes = 0
    largest = prime_numbers[0]
    smallest = prime_numbers[0]

    # Iterate through the list
    for prime in prime_numbers:
        sum_of_primes += prime
        if prime > largest:
            largest = prime
        if prime < smallest:
            smallest = prime

    # Return the results
    return sum_of_primes, largest, smallest, sorted(prime_numbers, reverse=True)