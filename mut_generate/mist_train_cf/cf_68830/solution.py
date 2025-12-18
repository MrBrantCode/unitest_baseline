"""
QUESTION:
Write a function get_memory_location in Python that takes two variables as input and returns their memory locations. Note that Python pre-allocates memory for integers from -5 to 256 for efficiency, so variables with values in this range will have the same memory location if they have the same value. Variables outside this range or with mutable types will have separate memory locations even if they have the same value.
"""

def get_memory_location(var1, var2):
    """
    This function returns the memory locations of two variables.
    
    Args:
        var1 (any): The first variable.
        var2 (any): The second variable.
    
    Returns:
        tuple: A tuple containing the memory locations of var1 and var2.
    """
    return id(var1), id(var2)