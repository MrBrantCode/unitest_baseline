"""
QUESTION:
Create a function `multiply_list` that takes a list of integers as input. For each integer in the list, if the number is prime, multiply it by 5. If the number is not prime, calculate the sum of its digits and multiply the sum by 2. The function should return a new list with the modified integers.
"""

def multiply_list(numbers):
    """
    This function takes a list of integers, multiplies prime numbers by 5, 
    and non-prime numbers by twice the sum of their digits.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list with modified integers.
    """

    def is_prime(num):
        """
        Helper function to check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    new_list = []
    for num in numbers:
        if is_prime(num):
            new_list.append(num * 5)
        else:
            digits_sum = sum(int(digit) for digit in str(num))
            new_list.append(digits_sum * 2)
    return new_list