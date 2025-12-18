"""
QUESTION:
Create a function `replace_and_count` that takes an input string and a dictionary of replacements as parameters. The dictionary should contain the old substrings as keys and their corresponding new substrings as values. The function should replace all occurrences of the old substrings with the new substrings in the input string and return the updated string along with a dictionary indicating the count of replacements made for each substring.
"""

def replace_and_count(input_string, replacements):
    """
    Replaces all occurrences of old substrings with new substrings in the input string 
    and returns the updated string along with a dictionary indicating the count of replacements made for each substring.

    Args:
        input_string (str): The original string to be updated.
        replacements (dict): A dictionary containing old substrings as keys and their corresponding new substrings as values.

    Returns:
        tuple: A tuple containing the updated string and a dictionary with replacement counts.
    """
    count_dict = {}
    for old, new in replacements.items():
        input_string, num_subs = input_string.replace(old, new), input_string.count(old)
        count_dict[old] = num_subs
    return input_string, count_dict