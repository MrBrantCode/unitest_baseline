"""
QUESTION:
Implement a function `filter_hidden` that takes a dictionary `x` as input and returns a new dictionary containing only the non-hidden items. Hidden files and directories are those whose names start with a dot ('.'). If a value in the dictionary is also a dictionary, the function should recursively filter its items. The input is guaranteed to be a nested dictionary.
"""

def filter_hidden(x: dict) -> dict:
    filtered_dict = {}
    for key, value in x.items():
        if not key.startswith('.'):
            if isinstance(value, dict):
                filtered_dict[key] = filter_hidden(value)
            else:
                filtered_dict[key] = value
    return filtered_dict