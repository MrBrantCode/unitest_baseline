"""
QUESTION:
Write a function `sum_divisible_by_three` that takes a list of integers as input and returns the sum of all numbers in the list that are both greater than 10 and divisible by 3.
"""

def sum_divisible_by_three(my_list):
    """
    Returns the sum of all numbers in the list that are both greater than 10 and divisible by 3.
    
    Args:
    my_list (list): A list of integers.
    
    Returns:
    int: The sum of all numbers in the list that are both greater than 10 and divisible by 3.
    """
    sum = 0
    for num in my_list:
        if num > 10 and num % 3 == 0:
            sum += num
    return sum