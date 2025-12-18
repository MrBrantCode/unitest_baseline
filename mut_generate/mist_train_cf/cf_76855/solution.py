"""
QUESTION:
Create a function called `filter_divisible_by_7` that takes a list of numbers as input and returns two separate lists: one containing numbers divisible by 7 and the other containing numbers not divisible by 7. The function should handle empty lists.
"""

def filter_divisible_by_7(input_list):
    """
    This function takes a list of numbers as input and returns two separate lists:
    one containing numbers divisible by 7 and the other containing numbers not divisible by 7.

    Args:
        input_list (list): A list of numbers.

    Returns:
        tuple: A tuple of two lists. The first list contains numbers divisible by 7,
               and the second list contains numbers not divisible by 7.
    """
    divisible_by_7 = [num for num in input_list if num % 7 == 0]
    not_divisible_by_7 = [num for num in input_list if num % 7 != 0]
    return divisible_by_7, not_divisible_by_7