"""
QUESTION:
Create a function named `arrange_prime_composite` that takes a list of unique positive integers as input and returns a list where all prime numbers come before composite numbers. In case of a tie, numbers should be sorted in descending order.
"""

def arrange_prime_composite(nums):
    """
    This function takes a list of unique positive integers and returns a list 
    where all prime numbers come before composite numbers. In case of a tie, 
    numbers are sorted in descending order.

    Args:
    nums (list): A list of unique positive integers.

    Returns:
    list: A list of integers where primes come before composites, sorted in descending order in case of a tie.
    """

    # Function to identify prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Separating prime and composite numbers
    primes = [i for i in nums if is_prime(i)]
    composites = [i for i in nums if not is_prime(i)]

    # Sorting them in descending order
    primes.sort(reverse=True)
    composites.sort(reverse=True)

    # Merging primes and composites
    result = primes + composites

    return result