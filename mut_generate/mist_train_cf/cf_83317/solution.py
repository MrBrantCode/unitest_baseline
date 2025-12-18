"""
QUESTION:
Create a function called `compact_dimensions` that takes an input of dimensions as an integer, and then returns the possible compactified dimensions for a given number of dimensions. The function should be able to handle both the string theory's 10 dimensions and M-theory's 11 dimensions.
"""

def compact_dimensions(dimensions: int) -> list:
    """
    Returns the possible compactified dimensions for a given number of dimensions.
    
    Args:
    dimensions (int): The number of dimensions.
    
    Returns:
    list: A list of possible compactified dimensions.
    """
    compactified_dimensions = []
    for i in range(1, dimensions):
        compactified_dimensions.append((i, dimensions - i))
    return compactified_dimensions