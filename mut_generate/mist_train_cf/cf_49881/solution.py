"""
QUESTION:
Create a function named `check_sorting` that takes a list or matrix as input and returns the type of sorting (ascending, descending, lexicographically, or unsorted). The function should handle lists containing diverse data types, nested lists, and matrices, and be able to manage null, undefined values, or empty lists/matrices. The function should have a low time and space complexity and be able to handle large inputs efficiently. Note that determining the exact sorting algorithm used and its time complexity is not feasible.
"""

def check_sorting(input_data):
    """
    Checks the type of sorting (ascending, descending, lexicographically, or unsorted) in a list or matrix.

    Args:
    input_data (list or matrix): The input list or matrix to check.

    Returns:
    str: The type of sorting (ascending, descending, lexicographically, or unsorted).
    """

    # Handle empty list or matrix
    if not input_data:
        return "Unsorted"

    # Handle null or undefined values
    if any(item is None for item in input_data):
        return "Unsorted"

    # Check if input data is a matrix
    if all(isinstance(i, list) for i in input_data):
        # Flatten the matrix into a list
        flattened_list = [item for sublist in input_data for item in sublist]
    else:
        flattened_list = input_data

    # Check for lexicographical sorting
    if all(isinstance(item, str) for item in flattened_list):
        if all(flattened_list[i] <= flattened_list[i + 1] for i in range(len(flattened_list) - 1)):
            return "Lexicographically"
        elif all(flattened_list[i] >= flattened_list[i + 1] for i in range(len(flattened_list) - 1)):
            return "Descending"
    # Check for numerical sorting
    else:
        if all(flattened_list[i] <= flattened_list[i + 1] for i in range(len(flattened_list) - 1)):
            return "Ascending"
        elif all(flattened_list[i] >= flattened_list[i + 1] for i in range(len(flattened_list) - 1)):
            return "Descending"
    return "Unsorted"