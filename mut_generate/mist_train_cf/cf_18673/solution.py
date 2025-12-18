"""
QUESTION:
Create a function `generate_multiples` that generates multiples of a prime number up to a given limit, excluding any multiples that are divisible by 5. The prime number should be greater than 1000 and less than 10000. The limit should be a number between 10000 and 50000.
"""

def generate_multiples(prime_number, limit):
    """
    Generates multiples of a prime number up to a given limit, excluding any multiples that are divisible by 5.
    
    Parameters:
    prime_number (int): A prime number greater than 1000 and less than 10000.
    limit (int): A number between 10000 and 50000.
    
    Returns:
    list: A list of multiples of the prime number up to the limit, excluding multiples divisible by 5.
    """
    return [i for i in range(prime_number, limit+1) if i % prime_number == 0 and i % 5 != 0]