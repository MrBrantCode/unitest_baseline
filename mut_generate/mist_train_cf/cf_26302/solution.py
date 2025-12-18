"""
QUESTION:
Create a function called `replace_first_instance` that takes three parameters: `target_string`, `string_to_replace`, and `replacement_string`. The function should replace the first occurrence of `string_to_replace` with `replacement_string` in `target_string`. Return the modified string.
"""

def replace_first_instance(target_string, string_to_replace, replacement_string):
    """
    Replaces the first occurrence of string_to_replace with replacement_string in target_string.

    Args:
        target_string (str): The original string.
        string_to_replace (str): The string to be replaced.
        replacement_string (str): The replacement string.

    Returns:
        str: The modified string.
    """
    return target_string.replace(string_to_replace, replacement_string, 1)