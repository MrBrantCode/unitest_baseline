"""
QUESTION:
Implement a function `process_variable_input` that takes a dictionary `variable_dict_input` and a string `variable_type` as input, and validates and processes the input according to the argument requirements specified in the `available_args` dictionary.

The `available_args` dictionary contains available arguments as keys and dictionaries with a 'required' key as values, indicating whether each argument is required or not. The function should validate the presence of required arguments, use default values if specified, and raise exceptions for missing or invalid arguments.

The function should return a dictionary containing the processed input arguments with their values.
"""

class MissingArgumentException(Exception):
    pass

class InvalidArgumentException(Exception):
    pass

def process_variable_input(variable_dict_input, variable_type, available_args):
    processed_input = {}
    for arg, details in available_args.items():
        if arg in variable_dict_input:
            processed_input[arg] = variable_dict_input[arg]
        elif details['required']:
            if 'default_value' in details:
                processed_input[arg] = details['default_value']
            else:
                raise MissingArgumentException(f"Missing required argument: {arg}")
        else:
            raise InvalidArgumentException(f"Invalid argument: {arg}")

    processed_input['variable_type'] = variable_type
    return processed_input