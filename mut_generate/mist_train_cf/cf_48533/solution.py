"""
QUESTION:
Write a function `find_max_and_sums` that takes a list of integers as input and returns the maximum number in the list, the sum of even numbers, and the sum of odd numbers. The function should use list comprehensions to compute the sums.
"""

def find_max_and_sums(nums):
    """
    This function finds the maximum number in the input list, 
    and returns it along with the sum of even numbers and the sum of odd numbers.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the maximum number, the sum of even numbers, and the sum of odd numbers.
    """
    max_num = max(nums)
    sum_even = sum(num for num in nums if num % 2 == 0)
    sum_odd = sum(num for num in nums if num % 2 != 0)
    
    return max_num, sum_even, sum_odd