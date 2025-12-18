"""
QUESTION:
Write a function `calculate_special_average` that calculates the average of numbers in a given list that meet the following conditions: 
- divisible by 3, 
- greater than 10, 
- have a digit sum greater than 15, 
- are prime numbers.

The function should return 0 if no numbers in the list meet the conditions.
"""

def calculate_special_average(numbers):
    """
    Calculate the average of numbers in a given list that meet the following conditions: 
    - divisible by 3, 
    - greater than 10, 
    - have a digit sum greater than 15, 
    - are prime numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The average of the numbers that meet the conditions, or 0 if no numbers meet the conditions.
    """

    def is_prime(n):
        """
        Check if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    # Initialize sum and count of numbers that meet the conditions
    total_sum = 0
    count = 0

    # Iterate over each number in the list
    for num in numbers:
        # Check if the number is divisible by 3, greater than 10, and has a digit sum greater than 15
        if num % 3 == 0 and num > 10 and sum(int(digit) for digit in str(num)) > 15:
            # Check if the number is prime
            if is_prime(num):
                # Add the number to the total sum and increment the count
                total_sum += num
                count += 1

    # Calculate the average if any numbers meet the conditions, otherwise return 0
    if count == 0:
        return 0
    else:
        return total_sum / count