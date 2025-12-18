"""
QUESTION:
Create a function named `generate_prime_multiples` that takes two integers as input, a prime number and a limit, and returns the list of multiples of the prime number up to the limit and the sum of these multiples. The function should not check if the input number is prime.
"""

def generate_prime_multiples(prime, limit):
    """
    Generate multiples of a prime number up to a given limit and return the list of multiples along with their sum.

    Args:
        prime (int): The prime number.
        limit (int): The upper limit.

    Returns:
        list, int: A list of multiples and their sum.
    """
    multiples = [i for i in range(prime, limit+1, prime)]
    sum_of_multiples = sum(multiples)
    return multiples, sum_of_multiples