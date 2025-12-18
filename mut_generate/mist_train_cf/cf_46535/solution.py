"""
QUESTION:
Create a function `get_even_prime_and_merge` that takes two lists of integers, `l1` and `l2`, as input and returns a list containing only the even prime numbers from both lists, merged and sorted in descending order. The function should skip negative numbers and consider a number as prime only if it is greater than 1 and has no divisors other than 1 and itself. 

Note: The function should be implemented with a helper function `is_prime` to check for primality, and a helper function `merge_and_sort` to merge and sort the lists.
"""

def get_even_prime_and_merge(l1: list, l2: list):
    """
    Return only even prime numbers from both lists, merged and sorted in descending order.
    """
    def is_prime(num: int):
        """Check if the number is a prime number"""
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqr = int(num**0.5) + 1
        for divisor in range(3, sqr, 2):
            if num % divisor == 0:
                return False
        return True

    even_prime_numbers = [num for num in l1 + l2 if num > 0 and num % 2 == 0 and is_prime(num)]
    return sorted(even_prime_numbers, reverse=True)