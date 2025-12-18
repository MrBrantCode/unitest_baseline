"""
QUESTION:
Create a function named `pascal_to_bar` that takes one argument, `pascal`, representing pressure in Pascals. The function should return the equivalent pressure in Bar, where 1 Bar is equal to 100,000 Pascals.
"""

def pascal_to_bar(pascal):
    """
    Converts pressure in Pascals to Bar.
    
    Parameters:
    pascal (float): Pressure in Pascals.
    
    Returns:
    float: Pressure in Bar.
    """
    return pascal / 100000