"""
QUESTION:
Create a function `prime_index_and_element` that takes a list of integers as input and returns `True` if all elements at prime indices in the list are prime numbers, and `False` otherwise. A prime index is defined as an index that is a prime number itself (e.g., 2, 3, 5, etc.). The function should not modify the input list.
"""

def prime_index_and_element(lst):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Iterating over each index in a list
    for idx,element in enumerate(lst):
        # Verify if index is a prime
        if is_prime(idx):
            # Verify if element in a list is a prime
            if not is_prime(element):
                # return false if element not a prime
                return False
    return True