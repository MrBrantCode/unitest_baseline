"""
QUESTION:
Implement the function `format_params` that takes a dictionary `params` as input and returns a dictionary where all nested dictionaries have been flattened. The keys of the nested dictionaries should be concatenated with their parent keys using a dot (.) to represent the hierarchy. Implement another function `format_params_string` that takes the output of `format_params` and returns a formatted string with each key-value pair on a new line, separated by a colon and a space.
"""

def format_params(params, parent_key='', sep='.'):
    items = []
    for key, value in params.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(format_params(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

def format_params_string(params):
    formatted_params = format_params(params)
    return '\n'.join([f"{key}: {value}" for key, value in formatted_params.items()])