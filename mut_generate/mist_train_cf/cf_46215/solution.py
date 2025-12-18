"""
QUESTION:
Write a function named `starts_one_ends(n)` that takes a positive integer `n` as input and returns the count of n-digit positive integers that start or end with 1 and are divisible by either 3 or 5, but not both.
"""

def starts_one_ends(n):
    """
    This function returns the count of n-digit positive integers that start or end with 1 
    and are divisible by either 3 or 5, but not both.

    Parameters:
    n (int): The number of digits in the integers to be checked.

    Returns:
    int: The count of n-digit positive integers that meet the conditions.
    """
    count = 0
    for i in range(10 ** (n - 1), 10 ** n):
        # Check if the number starts or ends with 1
        starts_with_1 = str(i).startswith("1")
        ends_with_1 = str(i).endswith("1")

        # Check if the number is divisible by 3 or 5 but not both
        divisible_by_3 = i % 3 == 0
        divisible_by_5 = i % 5 == 0
        divisible_by_15 = i % 15 == 0

        # Update the count if the conditions are met
        if (starts_with_1 or ends_with_1) and (divisible_by_3 != divisible_by_5):
            count += 1

    return count