"""
QUESTION:
Create a function called `first_two_chars` that takes one argument, which can be a string, list, or tuple. The function should return the first two elements of the input if it contains at least two elements. If the input has less than two elements, the function should return the message "Input is too short". If the input is not of type string, list, or tuple, the function should return the message "Invalid input type, expected string, list, or tuple".
"""

def first_two_chars(my_input):
    """
    Return the first two elements of a string/list/tuple if they contain at least two elements.
    Otherwise, an appropriate message will be returned.
    """
    if isinstance(my_input, (str, list, tuple)):
        if len(my_input) >= 2:
            return my_input[0:2]
        else:
            return "Input is too short"
    else:
        return "Invalid input type, expected string, list, or tuple"