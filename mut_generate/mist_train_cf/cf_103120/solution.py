"""
QUESTION:
Write a function named `get_prime_index_elements` that takes an array as input and returns a list of elements where the index is a prime number. The function should not take any additional arguments and the input array is 0-indexed.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_index_elements(arr):
    """
    Returns a list of elements from the input array where the index is a prime number.
    
    Args:
    arr (list): The input array.
    
    Returns:
    list: A list of elements from the input array where the index is a prime number.
    """
    prime_elements = [arr[i] for i in range(len(arr)) if is_prime(i)]
    return prime_elements