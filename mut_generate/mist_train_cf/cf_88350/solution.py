"""
QUESTION:
Write a function called `find_max_num` that takes a list of numbers as input and returns the maximum number in the list. The function should initialize a variable with the first element of the list and then iterate through the rest of the list to find the maximum number. The list must contain at least one element.
"""

def find_max_num(numbers):
    """
    This function finds the maximum number in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The maximum number in the list.
    """
    # Initialize max_num with the first element of the list
    max_num = numbers[0]

    # Iterate through each element in the list starting from the second element
    for num in numbers[1:]:
        # Check if the current element is greater than max_num
        if num > max_num:
            # Update max_num to the current element
            max_num = num

    # Return the maximum number in the list
    return max_num