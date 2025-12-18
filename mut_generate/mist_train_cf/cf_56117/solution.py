"""
QUESTION:
Design a function named `list_check` that takes a list `lst` and a value as input. The function should validate the presence of the value in the list and its nested lists, regardless of their nesting depth, and return a tuple containing a boolean indicating whether the value is present in all lists, the total count of lists containing the value, and the total number of occurrences of the value. The function should handle circular references, dictionaries, tuples, sets, and exceptions, and provide a meaningful error message if an exception occurs.
"""

def list_check(lst, value):
    """
    Validate the presence of a value in a list and its nested lists.
    
    Args:
    lst (list): The input list to search in.
    value: The value to search for.
    
    Returns:
    tuple: A tuple containing a boolean indicating whether the value is present in all lists,
           the total count of lists containing the value, and the total number of occurrences of the value.
    """
    
    visited_lists = set()
    presence_in_all = True
    total_lists = 0
    total_occurrences = 0

    def recursive_search(lst, value):
        nonlocal presence_in_all
        nonlocal total_lists
        nonlocal total_occurrences

        if id(lst) in visited_lists:
            return False
        visited_lists.add(id(lst))

        if isinstance(lst, dict):
            lst = lst.keys() | lst.values()

        current_presence = False
        for element in lst:
            if element == value:
                current_presence = True
                total_occurrences += 1
            if isinstance(element, (list, dict, set, tuple)):
                if recursive_search(element, value):
                    current_presence = True

        if current_presence:
            total_lists += 1
        else:
            presence_in_all = False

        return current_presence

    try:
        recursive_search(lst, value)
    except Exception as e:
        return f"An exception occurred: {str(e)}"
  
    return (presence_in_all, total_lists, total_occurrences)