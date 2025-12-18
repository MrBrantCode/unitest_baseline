"""
QUESTION:
Write a function `sum_of_multiples` that takes an integer `n` between 100 and 1000 (inclusive) as input. The function should calculate the sum of all numbers from 1 to `n` that are divisible by 3 or 5, and then check if the sum is a prime number. If the sum is prime, the function should print the sum. Estimate the time complexity of the `sum_of_multiples` function.
"""

def sum_of_multiples(n):
    """
    Calculate the sum of all numbers from 1 to `n` that are divisible by 3 or 5,
    and print the sum if it is a prime number.

    Args:
        n (int): An integer between 100 and 1000 (inclusive).

    Returns:
        None
    """

    # Initialize sum to 0
    total_sum = 0

    # Iterate through each number from 1 to n
    for i in range(1, n + 1):
        # If i is divisible by 3 or 5, add i to the sum
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    # Check if the sum is a prime number
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Print the sum if it is a prime number
    if is_prime(total_sum):
        print(total_sum)