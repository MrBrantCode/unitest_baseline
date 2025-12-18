"""
QUESTION:
Write a function called `find_odd_numbers` that takes a list of numbers as input. The function should return a new list containing only the odd numbers found in the input list. Additionally, it should print the total count of odd numbers and their corresponding positions in the original list.
"""

def find_odd_numbers(numbers):
    """
    Returns a list of odd numbers found in the input list and prints their count and positions.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of odd numbers.
    """
    odd_numbers = [num for num in numbers if num % 2 != 0]
    positions = [i for i, num in enumerate(numbers) if num % 2 != 0]

    print("Odd numbers found:", len(odd_numbers))
    print("Positions:", positions)
    print("New list:", odd_numbers)

    return odd_numbers