"""
QUESTION:
Create a function called `switch_statement(x)` that takes an integer `x` as input and returns a string. The function should use a switch statement to print and return "Zero", "One", "Two", "Three", "Four", or "Five" if `x` equals 0, 1, 2, 3, 4, or 5 respectively. If `x` is less than 0 or greater than 5, the function should print and return "Invalid".
"""

def switch_statement(x):
    """
    This function takes an integer x as input and returns a string.
    It uses a dictionary to mimic a switch statement and returns 
    "Zero", "One", "Two", "Three", "Four", or "Five" if x equals 
    0, 1, 2, 3, 4, or 5 respectively. If x is less than 0 or 
    greater than 5, the function returns "Invalid".

    Args:
        x (int): The input integer.

    Returns:
        str: The corresponding string based on the input integer.
    """

    # Create a dictionary to map integers to strings
    switch_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five"
    }

    # Use the get method of the dictionary to return the corresponding string
    # If the key is not found, return "Invalid"
    return switch_dict.get(x, "Invalid")