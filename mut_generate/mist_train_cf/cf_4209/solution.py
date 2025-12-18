"""
QUESTION:
Write a function `calculate_compound_interest(principal_amount, interest_rate, num_years, compounded_per_year)` that calculates the compound interest given the principal amount, rate of interest, number of years, and number of times interest is compounded per year. 

The function should take four arguments: `principal_amount` (positive number), `interest_rate` (positive number between 0 and 1), `num_years` (positive number), and `compounded_per_year` (positive integer). It should return the final amount after the specified number of years, considering compound interest, rounded to 2 decimal places.

The function should also handle invalid inputs: if any of the inputs are not positive numbers, or if `compounded_per_year` is not a positive integer, it should return an error message. Additionally, it should handle the case where `compounded_per_year` is zero to avoid division by zero.
"""

def calculate_compound_interest(principal_amount, interest_rate, num_years, compounded_per_year):
    """
    Calculate the compound interest given the principal amount, rate of interest, number of years, and number of times interest is compounded per year.

    Args:
    principal_amount (float): The initial amount of money.
    interest_rate (float): The interest rate (in decimal).
    num_years (float): The number of years the money is invested for.
    compounded_per_year (int): The number of times that interest is compounded per year.

    Returns:
    float: The final amount after the specified number of years, considering compound interest, rounded to 2 decimal places.
    str: An error message if any of the inputs are not positive numbers, or if compounded_per_year is not a positive integer.
    """

    # Input validation
    if principal_amount <= 0 or interest_rate <= 0 or num_years <= 0 or compounded_per_year <= 0:
        return "Error: All inputs must be positive numbers."

    # Calculate compound interest
    try:
        A = principal_amount * (1 + interest_rate/compounded_per_year) ** (compounded_per_year*num_years)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Round the final amount to 2 decimal places
    A = round(A, 2)

    return A