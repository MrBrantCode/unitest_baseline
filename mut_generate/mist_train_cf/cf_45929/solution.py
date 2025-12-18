"""
QUESTION:
Write a function `divisor_count_weighted_average` that takes three positive integer arguments: `n`, `m`, and `base`. The function should compute the weighted average of the integers from `n` through `m` (inclusive), with weights given by their divisors' count. Then, round the average to the nearest integer and convert that to the given custom base system. The custom base system should be another integer (`base`) in the range [2, 10] (inclusive). If `n` is greater than `m` or `base` is outside of the allowed range, return -1.
"""

from typing import Union

def divisor_count_weighted_average(n: int, m: int, base: int) -> Union[int, str]:
    """
    This function calculates the weighted average of integers from n to m (inclusive)
    with weights given by their divisors' count, rounds the average to the nearest integer,
    and converts it to a custom base system.

    Args:
    n (int): The start of the range (inclusive).
    m (int): The end of the range (inclusive).
    base (int): The custom base system (between 2 and 10).

    Returns:
    Union[int, str]: The rounded weighted average in the custom base system as a string, or -1 if the input is invalid.
    """

    # Check if n is greater than m or base is outside the allowed range
    if n > m or not 2 <= base <= 10:
        return -1

    # Initialize variables to store the sum of weighted numbers and the total weight
    weighted_sum = 0
    total_weight = 0

    # Iterate over the range from n to m
    for num in range(n, m + 1):
        # Calculate the number of divisors for the current number
        divisors = sum(1 for i in range(1, num + 1) if num % i == 0)

        # Add the weighted number to the sum and increment the total weight
        weighted_sum += num * divisors
        total_weight += divisors

    # Calculate the weighted average and round it to the nearest integer
    weighted_average = round(weighted_sum / total_weight)

    # Convert the weighted average to the custom base system
    converted_average = ""
    while weighted_average > 0:
        digit = weighted_average % base
        converted_average = str(digit) + converted_average
        weighted_average //= base

    # Add the base prefix to the converted average
    if base == 2:
        converted_average = "0b" + converted_average
    elif base == 8:
        converted_average = "0o" + converted_average
    else:
        converted_average = str(base) + converted_average

    return converted_average