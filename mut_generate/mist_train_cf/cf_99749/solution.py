"""
QUESTION:
Write a Python function named `swap_values` that takes two variables as input and returns a tuple containing the swapped values and their original data types. The function should be able to handle variables of different data types and store the variables in a tuple, list, or dictionary. If the variables are strings and complex numbers, the function should attempt to convert the string to a complex number before swapping the values.
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