"""
QUESTION:
Write a function `sum_excluding_multiples` that calculates the sum of numbers from 0 to n, excluding multiples of 3 and numbers that are multiples of both 2 and 5. The function should take an integer n as input and return the calculated sum.
"""

def sum_excluding_multiples(n):
    """
    This function calculates the sum of numbers from 0 to n, 
    excluding multiples of 3 and numbers that are multiples of both 2 and 5.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The calculated sum.
    """
    # Filter the numbers based on the given conditions using list comprehension
    filtered_numbers = [num for num in range(n + 1) if num % 3 != 0 and not (num % 2 == 0 and num % 5 == 0)]

    # Calculate the sum of the filtered numbers using the built-in sum() function
    sum_of_numbers = sum(filtered_numbers)

    return sum_of_numbers