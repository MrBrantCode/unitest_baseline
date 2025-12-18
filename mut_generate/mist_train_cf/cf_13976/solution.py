"""
QUESTION:
Create a list comprehension that filters pairs in a given list of tuples. The function should return pairs where the first element is a string and the second element is a prime number. The function should be able to handle a list of tuples as input.
"""

def filter_prime_pairs(my_list):
    """
    Filters pairs in a given list of tuples where the first element is a string and the second element is a prime number.
    
    Args:
        my_list (list): A list of tuples.
    
    Returns:
        list: A list of tuples with string and prime number pairs.
    """
    def is_prime(n):
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    
    return [(x, y) for x, y in my_list if isinstance(x, str) and is_prime(y)]