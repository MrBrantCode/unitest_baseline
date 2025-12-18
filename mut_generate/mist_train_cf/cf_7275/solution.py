"""
QUESTION:
Write a function called `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list that are greater than 100. The function should use a for loop to iterate through the list and check each number for primality.
"""

def sum_of_primes(numbers):
    """
    This function calculates the sum of all prime numbers in the input list that are greater than 100.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all prime numbers in the list that are greater than 100.
    """
    prime_sum = 0
    for num in numbers:
        if num > 100:
            is_prime = True
            for i in range(2, int(num/2) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_sum += num
    return prime_sum