"""
QUESTION:
Write a function sum_nineteen_seventeen_seq that calculates the total sum of all numbers less than a given positive integer m, where the numbers end with 9 and are divisible by either 17 or 19.
"""

def sum_nineteen_seventeen_seq(m: int) -> int:
    """
    This function calculates the total sum of all numbers less than a given positive integer 'm',
    where the numbers end with 9 and are divisible by either 17 or 19.

    Args:
        m (int): A positive integer.

    Returns:
        int: The total sum of the numbers that meet the conditions.
    """
    total_sum = 0
    for i in range(m):
        # Check if the last digit of the number is 9
        if str(i)[-1] == '9':
            # Check if the number is divisible by 17 or 19
            if i % 17 == 0 or i % 19 == 0:
                total_sum += i
    return total_sum