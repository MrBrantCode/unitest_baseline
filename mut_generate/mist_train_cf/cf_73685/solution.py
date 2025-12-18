"""
QUESTION:
Write a function `nearest_prime` that takes a list of numbers and a target value as input, and returns the prime number in the list that is closest to the target value. Assume that the input list contains at least one prime number and the target value is a positive integer. The function should have a time complexity of O(n^2) or better.
"""

# function to check if a number is prime
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def nearest_prime(numbers, target):
    """
    Returns the prime number in the list that is closest to the target value.

    Args:
    numbers (list): A list of numbers.
    target (int): The target value.

    Returns:
    int: The prime number closest to the target value.
    """
    primes = [num for num in numbers if is_prime(num)]
    closest_prime = min(primes, key=lambda x:abs(x-target))
    return closest_prime