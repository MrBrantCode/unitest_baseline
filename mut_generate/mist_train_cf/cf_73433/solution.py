"""
QUESTION:
Create a function construct_string that takes in two parameters c and d, and returns a formatted string in the form "Hello c World d!". The function should use Python's f-string formatting to insert the values of c and d into the string. The initial string should be "Hello" and "World" which will not change.
"""

def construct_string(c, d):
    """
    Returns a formatted string in the form "Hello c World d!".
    
    Parameters:
    c (str): The first variable to insert into the string.
    d (str): The second variable to insert into the string.
    
    Returns:
    str: A formatted string with the variables inserted.
    """
    return f"Hello {c} World {d}!"