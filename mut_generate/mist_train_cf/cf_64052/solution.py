"""
QUESTION:
Verify if a given list or matrix is sorted in ascending, descending, or lexicographical order. The function should handle lists containing various data types (integers, floats, strings) and nested lists or matrices. It should also manage exceptions due to different data types, null, undefined values, or empty lists/matrices. If the list or matrix is not sorted, return a suitable message. The function should be optimized for performance and handle large inputs efficiently.
"""

def is_sorted(data):
    """
    This function checks if a given list or matrix is sorted in ascending, descending, or lexicographical order.

    Args:
    data (list): A list or matrix containing various data types.

    Returns:
    str: A message indicating whether the list or matrix is sorted or not.
    """

    # Check if the input is a list
    if not isinstance(data, list):
        return "Error: Input is not a list."

    # Check if the list is empty
    if len(data) == 0:
        return "Error: List is empty."

    # Check if all elements in the list are of the same type
    if not all(isinstance(x, type(data[0])) for x in data):
        return "Error: List contains different data types."

    # Check if the list contains nested lists or matrices
    if isinstance(data[0], list):
        # Check if all sublists have the same length
        if not all(len(x) == len(data[0]) for x in data):
            return "Error: Sublists have different lengths."

        # Check if the sublists are sorted
        for i, sublist in enumerate(data):
            if not all(isinstance(x, type(sublist[0])) for x in sublist):
                return "Error: Sublist {} contains different data types.".format(i)

            if not is_sorted(sublist):
                return "Error: Sublist {} is not sorted.".format(i)

        # Check if the main list is sorted
        if all(data[i] <= data[i+1] for i in range(len(data)-1)):
            return "List is sorted in ascending order."
        elif all(data[i] >= data[i+1] for i in range(len(data)-1)):
            return "List is sorted in descending order."
        else:
            return "List is not sorted."

    else:
        # Check if the list contains any None or undefined values
        if any(x is None for x in data):
            return "Error: List contains None values."

        # Check if the list is sorted
        if all(data[i] <= data[i+1] for i in range(len(data)-1)):
            return "List is sorted in ascending order."
        elif all(data[i] >= data[i+1] for i in range(len(data)-1)):
            return "List is sorted in descending order."
        else:
            return "List is not sorted."