"""
QUESTION:
Write a function `power_lists(list1, list2)` that takes two lists of numbers (integers, floats, or complex numbers) as input and returns a new list where each element of `list1` is raised to the power of the corresponding element in `list2`. If `list2` is shorter than `list1`, the function should loop back to the start of `list2`. The function should handle potential exceptions, including invalid input types and division by zero.
"""

def power_lists(list1, list2):
    """
    Raises each element of list1 to the power of the corresponding element in list2.
    If list2 is shorter than list1, loops back to the start of list2.
    
    Args:
        list1 (list): The list of numbers to be raised.
        list2 (list): The list of powers.
    
    Returns:
        list: A new list with the results.
    """
    try:
        return [x**(list2[i % len(list2)]) for i, x in enumerate(list1)]
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs should be lists."
    except Exception as e:
        return "Error: " + str(e)