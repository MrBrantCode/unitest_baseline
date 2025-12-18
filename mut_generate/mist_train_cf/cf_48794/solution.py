"""
QUESTION:
Write a function `get_even_prime_and_merge(l1, l2)` that takes two lists of integers `l1` and `l2` as input. The function should return a list of even prime numbers that appear in either `l1` or `l2`, sorted in descending order. Note that 2 is the only even prime number.
"""

def get_even_prime_and_merge(l1, l2):
    """Return only even prime numbers from both lists, merged and sorted in descending order."""
    
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    even_prime_numbers = []
    for num in l1+l2:  
        if num == 2:  
            even_prime_numbers.append(num)

    return sorted(even_prime_numbers, reverse=True)