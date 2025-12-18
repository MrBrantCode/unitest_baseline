"""
QUESTION:
Create a function `repeat_strings` that takes two parameters: `str_list` and `num_list`, both of which are lists. The function should return a new list where each string in `str_list` is repeated according to the corresponding number in `num_list`. The function should ignore negative numbers in `num_list` and return an error message if `str_list` and `num_list` do not have the same number of elements.
"""

def repeat_strings(str_list, num_list):
    """
    Repeat strings in str_list according to corresponding numbers in num_list.

    Args:
        str_list (list): A list of strings to be repeated.
        num_list (list): A list of numbers specifying the repetition count for each string.

    Returns:
        list: A list of strings where each string in str_list is repeated according to the corresponding number in num_list.
        str: An error message if str_list and num_list do not have the same number of elements.
    """
    # Check if both lists have same amount of elements
    if len(str_list) != len(num_list):
        return "The two lists must have the same number of elements!"

    result = []
    for i in range(len(str_list)):
        # If the number is negative, simply ignore it
        if num_list[i] < 0:
            continue

        # Use list comprehension with extend for efficient concatenation
        result.extend([str_list[i]] * num_list[i])
        
    return result