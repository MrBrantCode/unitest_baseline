"""
QUESTION:
Create a function `generate_combinations(names, blanks)` that takes two lists, `names` and `blanks`, and returns a new list of composed strings. The function should integrate information from the two lists and conditionally format the strings based on the following criteria: exclude the combination of "Alice" and "cat". The `blanks` list contains strings with a double underscore (`__`) that should be replaced with the corresponding name.
"""

def generate_combinations(names, blanks):
    """
    Generate a list of composed strings by combining names and blanks.
    Exclude the combination of "Alice" and "cat".

    Args:
        names (list): A list of names.
        blanks (list): A list of strings with double underscores to be replaced.

    Returns:
        list: A list of composed strings.
    """
    return [name + blank[2:] for name in names for blank in blanks if not (name == "Alice" and "cat" in blank)]