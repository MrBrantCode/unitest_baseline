"""
QUESTION:
Determine the variable type of a given complex number expression and check its validity. 

Write a function named `check_complex_number` that takes a string expression as input, checks its validity, determines if it's a complex number, and outputs the variable type of the real and imaginary parts. The function should follow these rules:
- If the input contains any alphabets or special characters (except for '+', '-', 'j', and '.'), output "Invalid input".
- If the input does not contain both a real and imaginary part, output "Invalid input".
- Check if the real and imaginary parts are integers or floating-point numbers and output their respective types.
- If the input passes all checks, output the types of the real and imaginary parts, and "Complex number".
"""

def check_complex_number(expression):
    """
    Checks the validity of a complex number expression and determines the variable types of its real and imaginary parts.

    Args:
    expression (str): A string representing a complex number expression.

    Returns:
    tuple: A tuple containing the variable types of the real and imaginary parts, and a string indicating whether the input is a complex number.
    """

    # Remove leading and trailing whitespaces
    expression = expression.strip()

    # Check for invalid characters
    if not all(char in '+-0123456789.j ' for char in expression):
        return "Invalid input"

    # Split the expression into real and imaginary parts
    parts = expression.split('+')
    if len(parts) != 2 or 'j' not in parts[1]:
        parts = expression.split('-')
        if len(parts) != 2 or 'j' not in parts[1]:
            return "Invalid input"

    # Extract the real and imaginary parts
    real_part = parts[0].strip()
    imag_part = parts[1].strip().replace('j', '')

    # Check if the real and imaginary parts are numeric
    if not (real_part.replace('.', '', 1).isdigit() and imag_part.replace('.', '', 1).isdigit()):
        return "Invalid input"

    # Determine the variable types of the real and imaginary parts
    real_type = 'int' if '.' not in real_part else 'float'
    imag_type = 'int' if '.' not in imag_part else 'float'

    return f"{real_type} (real part), {imag_type} (imaginary part), Complex number"