"""
QUESTION:
Write a function `second_largest_number_and_frequency` that takes an array of integers as input and returns the second largest number and its frequency. If there are multiple numbers with the same frequency, return the smallest number among them. You cannot use any built-in sorting functions or data structures.
"""

def second_largest_number_and_frequency(nums):
    """
    This function finds the second largest number in the given array and its frequency.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the second largest number and its frequency.
    """
    
    # Initialize variables to keep track of the largest and second largest numbers and their frequencies
    largest = float('-inf')  # Negative infinity
    second_largest = float('-inf')
    largest_freq = 0
    second_largest_freq = 0

    # Iterate through each number in the array
    for num in nums:
        # If the current number is larger than largest, update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
            largest_freq = 1
            second_largest_freq = 0
        # If the current number is equal to largest, increment largest frequency
        elif num == largest:
            largest_freq += 1
        # If the current number is larger than second largest but not equal to largest, update second largest
        elif num > second_largest and num != largest:
            second_largest = num
            second_largest_freq = 1
        # If the current number is equal to second largest, increment second largest frequency
        elif num == second_largest:
            second_largest_freq += 1

    # Return the second largest number and its frequency
    return (second_largest, second_largest_freq)