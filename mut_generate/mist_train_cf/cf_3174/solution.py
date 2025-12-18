"""
QUESTION:
Replace odd numbers in a list with their squares and calculate the sum of even numbers.

Write a function, `replace_odd_with_square`, that takes a list of integers as input. Replace all odd numbers in the list with their squared values and calculate the sum of the even numbers. The function should return the sum of even numbers.
"""

def replace_odd_with_square(lst):
    """
    Replace odd numbers in the list with their squares and calculate the sum of even numbers.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The sum of even numbers in the list.
    """
    sum_of_even = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            sum_of_even += lst[i]
        else:
            lst[i] = lst[i] ** 2
    return sum_of_even