"""
QUESTION:
Create a Python function named `swap_values` that swaps the values of two variables, handles cases when the variables are of different data types, and returns the swapped values in a tuple along with the original data types of the variables. The function should be able to handle cases where one variable is a complex number and the other is a string by attempting to convert the string to a complex number. The input variables can be of any data type, and the function should not assume any specific input format.
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