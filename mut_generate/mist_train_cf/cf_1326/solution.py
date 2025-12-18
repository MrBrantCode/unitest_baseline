"""
QUESTION:
Write a function called `delete_even_numbers` that takes a list of integers and a boolean flag `in_place` as input. The function should delete all even numbers from the list if `in_place` is `True` or create a new list without even numbers if `in_place` is `False`. The function should handle cases where the input list is empty or contains no even numbers. The function should aim for a time complexity of O(log(n)) and space complexity of O(1).
"""

def delete_even_numbers(numbers, in_place=True):
    """
    Deletes all even numbers from the list if in_place is True or creates a new list without even numbers if in_place is False.

    Args:
        numbers (list): A list of integers.
        in_place (bool, optional): Whether to delete even numbers in-place or create a new list. Defaults to True.

    Returns:
        list: The updated list without even numbers if in_place is False.
    """
    if in_place:
        i = 0
        while i < len(numbers):
            if numbers[i] % 2 == 0:
                del numbers[i]
            else:
                i += 1
    else:
        return [num for num in numbers if num % 2 != 0]