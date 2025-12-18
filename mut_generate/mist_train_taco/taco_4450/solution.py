"""
QUESTION:
Write a function which converts the input string to uppercase.

~~~if:bf
For BF all inputs end with \0, all inputs are lowercases and there is no space between. 
~~~
"""

def convert_to_uppercase(input_string: str) -> str:
    """
    Converts the input string to uppercase.

    Parameters:
    input_string (str): The string to be converted to uppercase.

    Returns:
    str: The uppercase version of the input string.
    """
    return input_string.upper()