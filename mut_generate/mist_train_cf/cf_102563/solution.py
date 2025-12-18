"""
QUESTION:
Find and return the three largest unique numbers in the given array of integers, considering only one occurrence of each number, and with values ranging from -1000 to 1000. The output should be in descending order. If there are fewer than three unique numbers in the array, return an empty array.
"""

def three_largest_numbers(array):
    """
    Returns the three largest unique numbers in the given array of integers.

    Args:
    array (list): A list of integers ranging from -1000 to 1000.

    Returns:
    list: A list of the three largest unique numbers in descending order.
    If there are fewer than three unique numbers, an empty list is returned.
    """

    # Initialize an empty set to store unique numbers in the input array
    unique_numbers = set()

    # Iterate through the input array and add unique numbers to the set
    for num in array:
        unique_numbers.add(num)

    # Initialize an empty list to store the unique numbers in descending order
    unique_numbers_list = sorted(unique_numbers, reverse=True)

    # If the length of the list is less than 3, return an empty array
    if len(unique_numbers_list) < 3:
        return []

    # Otherwise, return the first three numbers in the list
    return unique_numbers_list[:3]