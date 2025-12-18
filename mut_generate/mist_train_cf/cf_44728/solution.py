"""
QUESTION:
Write a Python function `map_and_filter(input_list)` that takes a list of mixed data types and returns a new list containing only the integers that are either prime numbers or even. The function should filter out non-integer elements and apply the specified condition to integers.
"""

def map_and_filter(input_list):
    """
    This function filters the input list and returns a list of elements
    which are either prime numbers or even.
    """
    def is_prime_or_even(num):
        """
        Helper function checks if the number is prime or even.
        """
        # check if the number is even
        if num % 2 == 0:
            return True
        # check if the number is a prime
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    return [item for item in input_list if isinstance(item, int) and is_prime_or_even(item)]