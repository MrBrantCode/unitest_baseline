"""
QUESTION:
Create a function `find_odd_numbers` that takes three parameters: `start`, `end`, and `include_divisible_by_3`. This function should generate a list of odd numbers within the range of `start` to `end` (inclusive) based on the user's preference to include or exclude numbers divisible by 3. The function should not accept any invalid input.
"""

def find_odd_numbers(start, end, include_divisible_by_3):
    """
    This function generates a list of odd numbers within the range of `start` to `end` (inclusive)
    based on the user's preference to include or exclude numbers divisible by 3.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.
        include_divisible_by_3 (bool): A boolean indicating whether to include or exclude numbers divisible by 3.

    Returns:
        list: A list of odd numbers within the given range.
    """

    odd_numbers = [number for number in range(start, end + 1) if number % 2 != 0 
                   and (include_divisible_by_3 or number % 3 != 0)]
    
    return odd_numbers