"""
QUESTION:
Create a function `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the input list, preserving their original order. If the input list is empty, return "Input list is empty." The function should have a time complexity of O(n), where n is the length of the input list.
"""

def get_odd_numbers(input_list):
    """
    Returns a new list containing only the odd numbers from the input list, 
    preserving their original order. If the input list is empty, returns 
    "Input list is empty."
    
    Time complexity: O(n), where n is the length of the input list.
    
    Args:
        input_list (list): A list of integers.
    
    Returns:
        list or str: A list of odd numbers or "Input list is empty."
    """
    if len(input_list) == 0:
        return "Input list is empty."
    
    odd_numbers = []
    for num in input_list:
        if num % 2 != 0:
            odd_numbers.append(num)
    
    return odd_numbers