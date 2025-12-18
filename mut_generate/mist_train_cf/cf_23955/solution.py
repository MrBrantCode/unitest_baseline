"""
QUESTION:
Create a function `autocomplete` that takes in a list of possible inputs and the current input value. It should return the completed input if the current input value matches a prefix of an item in the list, otherwise return the original input value. The function should be case-insensitive and assume the list of possible inputs is not empty.
"""

def autocomplete(possible_inputs, current_input):
    """
    Autocomplete the current input value from a list of possible inputs.

    Args:
        possible_inputs (list): A list of possible input values.
        current_input (str): The current input value.

    Returns:
        str: The completed input value if the current input matches a prefix of an item in the list, 
             otherwise the original input value.
    """
    current_input_lower = current_input.lower()
    for item in possible_inputs:
        if item.lower().startswith(current_input_lower):
            return item
    return current_input