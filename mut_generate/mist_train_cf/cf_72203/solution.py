"""
QUESTION:
Implement a function that takes a string as input and returns a dictionary with the names of string methods as keys and their corresponding usage as values. The function should include the following methods: lower, upper, capitalize, title, replace, split, strip, startswith, endswith, and join.
"""

def string_methods(input_str):
    """
    This function returns a dictionary with string methods as keys and their usage as values.

    Parameters:
    input_str (str): The input string.

    Returns:
    dict: A dictionary containing string methods and their usage.
    """
    
    methods = {
        "lower": input_str.lower(),
        "upper": input_str.upper(),
        "capitalize": input_str.capitalize(),
        "title": input_str.title(),
        "replace": input_str.replace("world", "Python"),
        "split": input_str.split(","),
        "strip": input_str.strip(),
        "startswith": input_str.startswith("hello"),
        "endswith": input_str.endswith("world"),
        "join": "-".join(["hello", "world"])
    }
    
    return methods