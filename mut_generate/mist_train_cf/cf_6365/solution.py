"""
QUESTION:
Implement the `remove_odd_numbers` function, which takes a list of integers as input and returns the modified list with all odd numbers removed using the `remove()` method. The input list can contain up to 10^6 elements, including duplicates, and the solution must meet the following complexity requirements: time complexity less than O(n^2) and space complexity less than O(n).
"""

def remove_odd_numbers(lst):
    """
    Removes all odd numbers from the input list.

    Args:
        lst (list): A list of integers.

    Returns:
        list: The modified list with all odd numbers removed.
    """
    # Create a copy of the original list to avoid modifying it while iterating
    lst_copy = lst.copy()
    
    # Iterate over each number in the copied list
    for num in lst_copy:
        # Check if the number is odd
        if num % 2 != 0:
            # Remove the odd number from the original list
            lst.remove(num)
    return lst