"""
QUESTION:
Write a function named `sum_divisible_by_3_and_remainder_1` that calculates the sum of the numbers in the input list that are divisible by 3 and have a remainder of 1 when divided by 5. The function should only iterate over the input list once.
"""

def sum_divisible_by_3_and_remainder_1(nums):
    """
    This function calculates the sum of the numbers in the input list that are divisible by 3 and have a remainder of 1 when divided by 5.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The sum of numbers that are divisible by 3 and have a remainder of 1 when divided by 5.
    """
    
    # Initialize the sum to 0
    total_sum = 0

    # Iterate over each number in the array
    for num in nums:
        # Check if the number is divisible by 3 and has a remainder of 1 when divided by 5
        if num % 3 == 0 and num % 5 == 1:
            # If it satisfies both conditions, add it to the sum
            total_sum += num

    # Return the sum
    return total_sum