"""
QUESTION:
Create a function named `explode_string` that takes two parameters: `input_str` and `delimiter`. The function should split the input string into a list of elements using the given delimiter and then remove any leading or trailing whitespace characters from each element. The function should return the cleaned list of elements.
"""

def explode_string(input_str, delimiter):
    """Explode the input string into a list of elements using the given delimiter 
    and remove any leading or trailing whitespace characters from each element.

    Args:
        input_str (str): The input string to be exploded.
        delimiter (str): The delimiter used to split the input string.

    Returns:
        list: A list of cleaned elements.
    """
    exploded_list = input_str.split(delimiter)
    cleaned_list = [element.strip() for element in exploded_list]
    return cleaned_list