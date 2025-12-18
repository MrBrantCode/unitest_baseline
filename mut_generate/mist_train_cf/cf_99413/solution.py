"""
QUESTION:
Write a Python function named `merge_sorted_lists` that takes two lists, `odd_numbers` and `even_numbers`, as inputs. The function should return a new list that contains all the odd numbers in descending order followed by all the even numbers in ascending order. The input lists should be assumed to contain only integers.
"""

def merge_sorted_lists(odd_numbers, even_numbers):
    """
    This function merges two lists of integers, one containing odd numbers and the other containing even numbers.
    It returns a new list that contains all the odd numbers in descending order followed by all the even numbers in ascending order.
    
    Args:
        odd_numbers (list): A list of odd integers.
        even_numbers (list): A list of even integers.
    
    Returns:
        list: A new list with the desired order.
    """
    # Sort the lists
    odd_numbers.sort(reverse=True)
    even_numbers.sort()
    # Create a new list with the desired order
    return odd_numbers + even_numbers