"""
QUESTION:
Write a function named `solve_quadratic_equation` that takes the coefficients a, b, and c of a quadratic equation as input. The function should return the discriminant value and the roots of the quadratic equation. The function should also determine and indicate the nature of the roots (i.e., two distinct real roots, two equal real roots, or two complex roots).
"""

def solve_quadratic_equation(a, b, c):
    """
    This function calculates the discriminant and the roots of a quadratic equation.
    
    Parameters:
    a (float): The coefficient of the quadratic term.
    b (float): The coefficient of the linear term.
    c (float): The constant term.
    
    Returns:
    tuple: A tuple containing the discriminant value and the roots of the equation.
    """
    
    # Calculate the discriminant value
    discriminant = b**2 - 4*a*c
    
    # Determine the nature of the roots
    if discriminant > 0:
        nature = "Two distinct real roots"
    elif discriminant == 0:
        nature = "Two equal real roots"
    else:
        nature = "Two complex roots"
    
    # Calculate the roots using the quadratic formula
    if discriminant >= 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
    else:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        root1 = f"{real_part} + {imaginary_part}i"
        root2 = f"{real_part} - {imaginary_part}i"
    
    # Return the discriminant value and the roots
    return discriminant, root1, root2, nature