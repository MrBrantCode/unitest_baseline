"""
QUESTION:
Create a function called `delete_even_numbers` that takes a list of integers and a boolean flag `in_place` as input. The function should remove all even numbers from the list. If `in_place` is `True`, the function should modify the original list; otherwise, it should return a new list without the even numbers.
"""

def delete_even_numbers(numbers, in_place):
    """
    Deletes even numbers from a list of integers.

    Args:
        numbers (list): A list of integers.
        in_place (bool): A flag to indicate whether to modify the original list.

    Returns:
        list: The list without even numbers if in_place is False, otherwise None.
    """
    if in_place:
        numbers[:] = [num for num in numbers if num % 2 != 0]
    else:
        return [num for num in numbers if num % 2 != 0]