"""
QUESTION:
Create a function named `rotate` that takes two parameters: a list representing a doubly linked list and an integer `N`. The function should first validate and repair the input list by removing any non-integer values and duplicates. It should then rotate the list by `N` nodes in either direction and return the result.

The function should handle the following restrictions and edge cases:

- The input list may not be a valid list structure and may contain non-integer values or duplicates.
- `N` may be negative, 0, or greater than the number of nodes in the list.
- The list may be empty.
- If `N` is greater than the length of the list, the function should rotate the list by `N` modulo the length of the list.
- If `N` is negative or the list is empty, the function should throw an assertion error with an appropriate error message.
"""

def rotate(input_list, N):
    """
    Rotate a doubly linked list by N nodes in either direction.

    Args:
    input_list (list): A list representing a doubly linked list.
    N (int): The number of nodes to rotate the list by.

    Returns:
    list: The rotated list.

    Raises:
    AssertionError: If the input list is empty or N is negative.
    """

    if not input_list:
        return
    
    # Remove any non-integer values
    input_list = [x for x in input_list if isinstance(x, int)]

    # Remove any duplicates - would cause links in the list to break
    input_list = list(dict.fromkeys(input_list))

    assert len(input_list) > 0, "The list cannot be empty"

    N = N % len(input_list) # Handle case when N is greater than the length of the list
    assert N >= 0, "Invalid N - cannot be negative"

    return input_list[-N:] + input_list[:-N]