"""
QUESTION:
Implement the function `rounded_avg_custom_base(n, m, base)` to calculate the custom base representation based on the given weighted averages, divisors' count, and arithmetic progression sum. The function should take three positive integers `n`, `m`, and `base` as input, where `n` and `m` represent the range [n, m] (inclusive) and `base` represents the custom base system (ranging from 2 to 10). If `n` is greater than `m` or `base` is outside of the allowed range (2 to 10), return -1.
"""

from typing import Union

def rounded_avg_custom_base(n: int, m: int, base: int) -> Union[int, str]:
    """
    Calculate the custom base representation based on the given weighted averages, 
    divisors' count, and arithmetic progression sum.

    Args:
        n (int): The start of the range (inclusive).
        m (int): The end of the range (inclusive).
        base (int): The custom base system (ranging from 2 to 10).

    Returns:
        Union[int, str]: The custom base representation as a string if the input is valid, -1 otherwise.
    """

    # Check if n is greater than m or base is outside of the allowed range (2 to 10)
    if n > m or not 2 <= base <= 10:
        return -1

    # Initialize variables to store the sum of numbers and the sum of divisors' count
    total_sum = 0
    total_divisors = 0

    # Iterate over the range from n to m (inclusive)
    for num in range(n, m + 1):
        # Calculate the divisors' count of the current number
        divisors = sum(1 for i in range(1, num + 1) if num % i == 0)

        # Add the number multiplied by its divisors' count to the total sum
        total_sum += num * divisors
        # Add the divisors' count to the total divisors
        total_divisors += divisors

    # Calculate the weighted average and round it to the nearest integer
    weighted_avg = round(total_sum / total_divisors)

    # Calculate the sum of the arithmetic progression up to the given integer limit
    progression_sum = sum(weighted_avg + i for i in range(m - n + 1))

    # Convert the sum of the arithmetic progression to the custom base system
    custom_base = ""
    while progression_sum > 0:
        custom_base = str(progression_sum % base) + custom_base
        progression_sum //= base

    # Add the base prefix to the custom base representation
    custom_base = f"0b{custom_base}" if base == 2 else f"0o{custom_base}" if base == 8 else f"{base}#{custom_base}"

    return custom_base