"""
QUESTION:
Write a Python function named `swap_values` that takes two variables as input, swaps their values, and returns the swapped values along with their original data types in a tuple. The function should handle variables of different data types, including complex numbers and strings. The function should also be able to handle inputs in the format of a dictionary, a list, or a tuple, but does not need to handle SQL database operations.

The function should return a tuple containing the swapped values and their original data types, with the original data types being the types of the input variables before any potential conversion.
"""

def swap_values(var1, var2):
    # Get original data types
    type1 = type(var1)
    type2 = type(var2)
    
    # Convert string to complex number if necessary
    if isinstance(var1, str) and isinstance(var2, complex):
        try:
            var1 = complex(var1)
        except ValueError:
            pass
    elif isinstance(var2, str) and isinstance(var1, complex):
        try:
            var2 = complex(var2)
        except ValueError:
            pass
        
    # Swap values
    var1, var2 = var2, var1
    
    # Return swapped values and original data types
    return (var1, var2, type1, type2)