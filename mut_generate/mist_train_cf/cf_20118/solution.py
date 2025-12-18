"""
QUESTION:
Write a function `calculate_frequencies_and_operations` that takes a list of integers as input and returns four values: the frequency of numbers divisible by 3, the frequency of numbers not divisible by 3, the sum of all numbers divisible by 3, and the product of all numbers not divisible by 3. The function should handle negative numbers correctly.
"""

def calculate_frequencies_and_operations(list_of_ints):
    """
    This function calculates the frequency of numbers divisible by 3, 
    the frequency of numbers not divisible by 3, 
    the sum of all numbers divisible by 3, and 
    the product of all numbers not divisible by 3.
    
    Args:
        list_of_ints (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the frequency of numbers divisible by 3, 
               the frequency of numbers not divisible by 3, 
               the sum of all numbers divisible by 3, and 
               the product of all numbers not divisible by 3.
    """
    divisible_by_3_count = 0
    not_divisible_by_3_count = 0
    divisible_by_3_sum = 0
    not_divisible_by_3_product = 1
    
    for num in list_of_ints:
        if num % 3 == 0:
            divisible_by_3_count += 1
            divisible_by_3_sum += num
        else:
            not_divisible_by_3_count += 1
            not_divisible_by_3_product *= num
    
    return divisible_by_3_count, not_divisible_by_3_count, divisible_by_3_sum, not_divisible_by_3_product