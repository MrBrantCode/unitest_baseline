"""
QUESTION:
Write a function named `swap_values` that takes two input variables of any data type, swaps their values, and returns the swapped values along with their original data types in a tuple. The input variables can be in any format (e.g., dictionary, list, tuple). The function should handle cases where the input variables have different data types, including complex numbers and strings, and attempt to convert strings to complex numbers if possible.
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