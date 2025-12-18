"""
QUESTION:
Compute the average of a list of numbers excluding any numbers that are divisible by 5 and also contain the digit 7. The function should be named 'avg_exclude_numbers' and it should take a list of integers as input and return a float representing the calculated average.
"""

def avg_exclude_numbers(nums):
    """
    Compute the average of a list of numbers excluding any numbers that are divisible by 5 and also contain the digit 7.

    Args:
        nums (list): A list of integers.

    Returns:
        float: The calculated average.
    """
    # Filter out numbers that are divisible by 5 and contain the digit 7
    filtered_nums = [num for num in nums if not (num % 5 == 0 and '7' in str(num))]
    
    # Check if there are any numbers left after filtering
    if not filtered_nums:
        return 0.0
    
    # Calculate the sum of the remaining numbers
    total = sum(filtered_nums)
    
    # Calculate the average
    average = total / len(filtered_nums)
    
    return average