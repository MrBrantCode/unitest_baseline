"""
QUESTION:
Create a function `insert_elements_at` that takes a list of tuples as a parameter where each tuple contains an index and a value to be inserted at that index in the global list. The function should handle insertion at negative indices and check for invalid indices. The function should sort the input list of tuples in descending order to handle changing indices due to insertions.
"""

def insert_elements_at(initial_list, indices_values):
    """
    Inserts elements at specified indices in the given list.

    Args:
    initial_list (list): The list where elements will be inserted.
    indices_values (list): A list of tuples containing index and value to be inserted.

    Returns:
    list: The updated list after insertion.
    """

    indices_values.sort(reverse=True)  # sorting in reverse to handle the changing index problem

    for index, value in indices_values:
        if index < -len(initial_list) or index > len(initial_list):
            print(f"Invalid index: {index}")
        else:
            if index < 0:
                index += len(initial_list)  # convert negative index into positive
            initial_list.insert(index, value)

    return initial_list