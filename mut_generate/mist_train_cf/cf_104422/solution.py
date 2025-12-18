"""
QUESTION:
Write a function named `find_primes_and_sum` that generates an array of all prime numbers between 1 and 100 and returns the array along with the sum of those prime numbers.
"""

def find_primes_and_sum(limit):
    """
    Generates an array of all prime numbers between 1 and the given limit, 
    and returns the array along with the sum of those prime numbers.

    Args:
        limit (int): The upper limit for finding prime numbers.

    Returns:
        tuple: A tuple containing a list of prime numbers and their sum.
    """
    primes = []
    total_sum = 0

    for num in range(2, limit + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            total_sum += num

    return primes, total_sum