"""
QUESTION:
Write a function `weighted_average` that calculates the weighted average of a list of integers. The weight of each number is determined by its index in the list, with the first number having a weight of 1, the second number having a weight of 2, and so on. Exclude any negative numbers from the calculation and return the weighted average.
"""

def weighted_average(numbers):
    """
    This function calculates the weighted average of a list of integers.
    The weight of each number is determined by its index in the list, 
    with the first number having a weight of 1, the second number having a weight of 2, and so on.
    Exclude any negative numbers from the calculation and return the weighted average.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The weighted average of the list of integers.
    """

    total_weighted_sum = 0  # Initialize sum as 0.
    total_weight = 0  # Initialize weight as 0.
    count = 1  # Initialize count as 1.

    for number in numbers:  # For each number in the list:
        if number < 0:  # If the number is negative, skip to the next number.
            continue
        total_weighted_sum += number * count  # Multiply the number by its corresponding weight (count) and add to sum.
        total_weight += count  # Increment the weight by count.
        count += 1  # Increment the count by 1.

    if total_weight == 0:  # Check if total weight is zero to avoid division by zero error.
        return 0  # Return zero if total weight is zero.

    weighted_average = total_weighted_sum / total_weight  # Calculate the weighted average.
    return weighted_average  # Return the weighted average.