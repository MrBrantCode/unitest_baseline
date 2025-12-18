"""
QUESTION:
Write a function named PrimeNumbers that takes a list of integers as input and returns a list of prime numbers from the input list. The function should check if each number in the list is prime and append it to the output list if it is prime. Analyze the runtime complexity of this function.
"""

def PrimeNumbers(items):
    """
    This function takes a list of integers as input, filters out the prime numbers and returns them as a list.

    Args:
        items (list): A list of integers.

    Returns:
        list: A list of prime numbers from the input list.
    """

    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return [item for item in items if is_prime(item)]