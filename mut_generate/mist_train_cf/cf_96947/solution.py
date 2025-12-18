"""
QUESTION:
Create a function named `is_prime` that prints all prime numbers within a given range in ascending order. The function should take two parameters: `lower_range` and `upper_range`. The function should return no value (i.e., it should print the result directly) and should not use any input from the user.
"""

def is_prime(lower_range, upper_range):
    """
    Prints all prime numbers within a given range in ascending order.

    Parameters:
    lower_range (int): The lower bound of the range (inclusive).
    upper_range (int): The upper bound of the range (inclusive).

    Returns:
    None
    """
    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in range(lower_range, upper_range + 1) if check_prime(num)]
    prime_numbers.sort()
    for prime in prime_numbers:
        print(prime)