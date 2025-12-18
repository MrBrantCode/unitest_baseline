"""
QUESTION:
Write a function `complex_number_type(expression)` that determines the type of a given complex number expression. The function should return a string indicating the type of the real and imaginary parts, and whether the expression is a complex number or not.

Restrictions:
- The input expression should only contain digits, '+', '.', and 'j'.
- The expression should be in the format 'real_part + imaginary_partj', where real_part and imaginary_part are integers or floating-point numbers.
- If the input expression is invalid, return "Invalid input".
"""

def complex_number_type(expression):
    """
    This function determines the type of a given complex number expression.

    Args:
    expression (str): A string representing a complex number in the format 'real_part + imaginary_partj'.

    Returns:
    str: A string indicating the type of the real and imaginary parts, and whether the expression is a complex number or not.
    """
    try:
        # Remove the '+' sign from the expression to split it into real and imaginary parts
        parts = expression.replace('+', ' ').split()
        
        # Check if 'j' is present in the second part to confirm it's the imaginary part
        if 'j' not in parts[1]:
            return "Invalid input"
        
        # Extract the real and imaginary parts
        real_part = parts[0]
        imaginary_part = parts[1].replace('j', '')
        
        # Check if both parts are numeric (either integer or float)
        if not (real_part.replace('.', '', 1).isdigit() and imaginary_part.replace('.', '', 1).isdigit()):
            return "Invalid input"
        
        # Determine the type of the real and imaginary parts
        real_type = 'integer' if '.' not in real_part else 'float'
        imaginary_type = 'integer' if '.' not in imaginary_part else 'float'
        
        # Return the type of the complex number
        return f"The complex number is {real_type} + {imaginary_type}j"
    except Exception as e:
        return "Invalid input"