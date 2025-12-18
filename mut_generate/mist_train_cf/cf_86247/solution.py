"""
QUESTION:
Create a function that generates a list of all prime numbers between 1 and 10,000, then calculates and returns the sum, average, and count of the prime numbers. The function should be named `is_prime_and_calculate` or similar. The input of the function should be the upper limit of the range (in this case, 10,000), and the output should be the sum, average, and count of the prime numbers in that range.
"""

def calculate_primes(limit):
    """
    Generates a list of prime numbers up to the given limit, 
    then calculates and returns their sum, average, and count.

    Args:
    limit (int): The upper limit for generating prime numbers.

    Returns:
    tuple: A tuple containing the sum, average, and count of prime numbers.
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [num for num in range(2, limit + 1) if is_prime(num)]
    prime_sum = sum(prime_numbers)
    prime_average = prime_sum / len(prime_numbers)
    prime_count = len(prime_numbers)

    return prime_sum, prime_average, prime_count