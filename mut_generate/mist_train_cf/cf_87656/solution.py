"""
QUESTION:
Create a function named `sum_of_primes_in_range` that takes two parameters, `start` and `end`, representing the start and end of a range, and calculates the sum of all prime numbers within this range (inclusive). The function should also print each prime number in the range. The function should not take any other parameters and should not use any external libraries.
"""

def sum_of_primes_in_range(start, end):
    """
    Calculate the sum of all prime numbers within a given range (inclusive) and print each prime number.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        int: The sum of all prime numbers within the given range.
    """

    prime_sum = 0
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)
                prime_sum += num

    return prime_sum