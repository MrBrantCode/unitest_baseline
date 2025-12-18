"""
QUESTION:
Retrieve the elements in an array where both the index and the element are prime numbers. Write a function that takes an array as input and returns a list of elements that meet this condition. The function should be able to handle arrays of any length.
"""

def retrieve_prime_elements(arr):
    """
    Retrieves the elements in an array where both the index and the element are prime numbers.

    Args:
        arr (list): The input array.

    Returns:
        list: A list of elements that meet the condition.
    """
    def is_prime(num):
        # Check if a number is prime
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = [element for index, element in enumerate(arr) if is_prime(index) and is_prime(element)]
    return result