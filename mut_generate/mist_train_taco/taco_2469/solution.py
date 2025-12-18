"""
QUESTION:
I will give you two strings. I want you to transform stringOne into stringTwo one letter at a time.

Example:
"""

def generate_string_mutations(stringOne, stringTwo):
    """
    Generates a sequence of string mutations transforming stringOne into stringTwo one letter at a time.

    Parameters:
    stringOne (str): The initial string.
    stringTwo (str): The target string.

    Returns:
    str: A string containing all intermediate transformations, each on a new line.
    """
    return '\n'.join([stringOne] + [stringTwo[:i] + stringOne[i:] for (i, (a, b)) in enumerate(zip(stringOne, stringTwo), 1) if a != b]) + '\n'