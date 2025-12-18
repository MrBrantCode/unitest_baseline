"""
QUESTION:
Create a function `sum_of_first_three_even_numbers` that takes a list of integers as input. The function should return the sum of the first three even numbers in the sorted list of even numbers from the input list. If the list contains less than three even numbers, return the sum of all the even numbers.
"""

def sum_of_first_three_even_numbers(arr):
    """
    This function takes a list of integers as input, 
    and returns the sum of the first three even numbers 
    in the sorted list of even numbers from the input list.
    
    If the list contains less than three even numbers, 
    it returns the sum of all the even numbers.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of the first three even numbers in the sorted list.
    """
    even_numbers = [num for num in arr if num % 2 == 0]
    sorted_even_numbers = sorted(even_numbers)
    sum_first_three = sum(sorted_even_numbers[:3])
    return sum_first_three