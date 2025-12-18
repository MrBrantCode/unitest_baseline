"""
QUESTION:
Write a function `polar_to_cartesian` that converts a given polar equation of the form r = f(θ) into a Cartesian equation. The function should take as input the coefficients of sin(θ) and cos(θ) in the polar equation. In this case, the function should convert the polar equation r = 2 sin(θ) + cos(θ) into a Cartesian equation.
"""

def polar_to_cartesian(sin_coeff, cos_coeff):
    """
    Convert a given polar equation of the form r = sin_coeff * sin(θ) + cos_coeff * cos(θ) 
    into a Cartesian equation.

    Parameters:
    sin_coeff (float): The coefficient of sin(θ) in the polar equation.
    cos_coeff (float): The coefficient of cos(θ) in the polar equation.

    Returns:
    A string representing the Cartesian equation equivalent to the input polar equation.
    """

    # convert to cartesian coordinates
    x = f"{sin_coeff} * sin(2θ) + {cos_coeff}**2 * cos²(θ)"
    y = f"{sin_coeff} * sin²(θ) + {sin_coeff} * cos(θ)sin(θ)"

    # return cartesian equation
    return f"x = {x}, y = {y}"

# renamed the function to match the question