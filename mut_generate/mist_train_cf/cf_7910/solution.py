"""
QUESTION:
Write a function `get_sorted_odd_numbers` that takes a list of elements as input, filters out non-integer and even elements, and returns a new list containing only the odd integers in descending order. The function should not modify the original list and should have a time complexity of O(nlogn) or better.
"""

def get_sorted_odd_numbers(input_list):
    """
    This function filters out non-integer and even elements from the input list, 
    and returns a new list containing only the odd integers in descending order.

    Args:
        input_list (list): A list of elements

    Returns:
        list: A list of odd integers in descending order
    """
    odd_numbers = [num for num in input_list if isinstance(num, int) and num % 2 != 0]
    return sorted(odd_numbers, reverse=True)