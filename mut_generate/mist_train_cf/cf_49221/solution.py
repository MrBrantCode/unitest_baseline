"""
QUESTION:
Write a function named `concatenate_list` that takes a list as input, which can contain strings and/or nested lists of any depth. The function should return a single string with all the strings in the input list concatenated together, separated by a comma and a space, while ignoring any non-string and non-list items.
"""

def concatenate_list(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            # The item is a list, so concatenate its contents
            result.append(concatenate_list(item))
        elif isinstance(item, str):
            # The item is a string, so just add it to the result
            result.append(item)
        else:
            # The item is not a string or a list, so print a warning message
            print(f"Warning: Ignoring unexpected data type: {item}")

    # Concatenate all the strings in the result list, separated by a comma and a space
    return ', '.join(result)