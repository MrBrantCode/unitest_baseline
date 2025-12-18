"""
QUESTION:
Write a function called `remove_first_even_divisible_by_3_and_5` that takes a list of at least 5 unique integers as input and returns the list with the first even number that is divisible by both 3 and 5 removed. If no such number exists, return the original list. The returned list should be sorted in descending order.
"""

def remove_first_even_divisible_by_3_and_5(nums):
    """
    This function removes the first even number that is divisible by both 3 and 5 from a given list.
    If no such number exists, it returns the original list. The returned list is sorted in descending order.

    Args:
        nums (list): A list of unique integers.

    Returns:
        list: The list with the first even number that is divisible by both 3 and 5 removed, sorted in descending order.
    """

    # Find the index of the first even number that is divisible by both 3 and 5
    for i, num in enumerate(nums):
        if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
            # Remove the number from the list
            nums.pop(i)
            break

    # Sort the list in descending order
    nums.sort(reverse=True)

    return nums