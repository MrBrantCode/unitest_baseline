"""
QUESTION:
Create a function `get_even_prime_and_merge(l1: list, l2: list)` that merges two lists, filters out the even prime numbers, and returns them in descending order. 

The function should use two helper functions: `merge_and_sort(m: list, n: list)` to merge and sort the lists in descending order, and `is_prime(x: int)` to check if a number is prime. The `is_prime(x: int)` function should return `True` if the number is prime and `False` otherwise. 

The `get_even_prime_and_merge(l1: list, l2: list)` function should ignore integers that do not satisfy the prime number validity checks.
"""

def get_even_prime_and_merge(l1: list, l2: list):
    """Return only even prime numbers from both lists, merged and sorted in descending order."""
    
    def merge_and_sort(m: list, n: list):
        result = m + n
        result.sort(reverse=True)
        return result

    def is_prime(x: int):
        if x <= 1 or x % 2 == 0: 
            return x == 2     # return False
        sqr = int(x**0.5) + 1
        for divisor in range(3, sqr, 2):
            if x % divisor == 0:
                return False
        return True

    even_prime_numbers = []
    for num in merge_and_sort(l1, l2):
        if num > 1 and num % 2 == 0 and is_prime(num):
            even_prime_numbers.append(num)

    return even_prime_numbers