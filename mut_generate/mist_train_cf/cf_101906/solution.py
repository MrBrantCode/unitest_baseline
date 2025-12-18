"""
QUESTION:
Write a function named `swap_values` that swaps the values of two variables of any data type, including complex numbers and strings. The function should accept the variables in any format, including dictionary, list, or tuple, and return the swapped values in a tuple along with their original data types.
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