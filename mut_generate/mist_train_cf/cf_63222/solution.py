"""
QUESTION:
Design a Python function called `extract_last` that takes one argument, `input_list`, which should be a list containing elements of any type. The function should return a tuple containing the mutated list after removing its last element and the removed element itself. If the input is not a list, the function should return an error message. If the input list is empty, the function should also return an error message.
"""

def extract_last(input_list):
    # Error handling: check if input is a list
    if not isinstance(input_list, list):
        return 'Error: Input must be a list.'
    # Handle empty list scenario
    elif not input_list:
        return 'Error: Input list is empty.'
    else:
        # Extract the last element
        last_element = input_list[-1]
        # Mutate the list
        mutated_list = input_list[:-1]
        return mutated_list, last_element