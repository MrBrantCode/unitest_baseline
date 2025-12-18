"""
QUESTION:
Write a function named `last_three_elements` that takes a list of integers as input and returns the last three elements if they meet the following conditions:
- Their sum is greater than 10.
- Their product is divisible by 5.
- All three elements are prime numbers.
The function should return the last three elements if all conditions are met, otherwise, return None or a message indicating that no elements satisfy the conditions.
"""

def last_three_elements(nums):
    """
    This function checks the last three elements of a list and returns them if their sum is greater than 10, 
    their product is divisible by 5, and all three elements are prime numbers.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The last three elements of the list if they meet the conditions, otherwise None.
    """

    # Check if the list has at least three elements
    if len(nums) < 3:
        return None

    # Get the last three elements of the list
    last_three = nums[-3:]

    # Function to check if a number is prime
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check if all elements are prime
    if not all(is_prime(num) for num in last_three):
        return None

    # Check if the sum of the last three elements is greater than 10
    if sum(last_three) <= 10:
        return None

    # Check if the product of the last three elements is divisible by 5
    if (last_three[0] * last_three[1] * last_three[2]) % 5 != 0:
        return None

    # If all conditions are met, return the last three elements
    return last_three