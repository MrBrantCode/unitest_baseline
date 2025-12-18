"""
QUESTION:
Create a function `combine_sorted_lists` that takes two lists of integers, `odd_numbers` and `even_numbers`, as inputs, where `odd_numbers` contains all odd numbers between 1 and 50 and `even_numbers` contains all even numbers between 1 and 50. The function should return a new list that contains all the odd numbers in descending order followed by all the even numbers in ascending order. The function should not print or display any output; it should only return the new list.
"""

def combine_sorted_lists(odd_numbers, even_numbers):
    """
    Combine two lists of integers, one containing odd numbers and the other containing even numbers,
    into a new list with the odd numbers in descending order followed by the even numbers in ascending order.

    Args:
        odd_numbers (list): A list of integers containing all odd numbers between 1 and 50.
        even_numbers (list): A list of integers containing all even numbers between 1 and 50.

    Returns:
        list: A new list containing all the odd numbers in descending order followed by all the even numbers in ascending order.
    """
    # Sort the lists
    odd_numbers.sort(reverse=True)
    even_numbers.sort()
    # Create a new list with the desired order
    new_list = odd_numbers + even_numbers
    return new_list