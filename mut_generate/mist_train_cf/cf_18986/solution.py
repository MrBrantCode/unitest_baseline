"""
QUESTION:
Write a function called `calculate_compound_interest` that takes in four parameters: `principal_amount`, `interest_rate`, `num_years`, and `compounded_per_year`. This function should calculate the final amount after the specified number of years, considering compound interest, and return the result rounded to 2 decimal places. The function should also include input validation to ensure that all inputs are positive numbers and handle potential division by zero errors. If any input is invalid or an error occurs, the function should return an error message.
"""

def calculate_compound_interest(principal_amount, interest_rate, num_years, compounded_per_year):
    """
    Calculate the final amount after the specified number of years, considering compound interest.

    Args:
        principal_amount (float): The initial amount of money
        interest_rate (float): The interest rate
        num_years (int): The number of years
        compounded_per_year (int): The number of times interest is compounded per year

    Returns:
        float: The final amount after the specified number of years, rounded to 2 decimal places
        str: An error message if any input is invalid or an error occurs
    """

    # Input validation
    if principal_amount <= 0:
        return "Principal amount must be a positive number."
    if interest_rate <= 0:
        return "Interest rate must be a positive number."
    if num_years <= 0:
        return "Number of years must be a positive number."
    if compounded_per_year <= 0:
        return "Number of times interest is compounded per year must be a positive number."

    # Calculate compound interest
    try:
        A = principal_amount * (1 + interest_rate / compounded_per_year) ** (compounded_per_year * num_years)
        return round(A, 2)
    except ZeroDivisionError:
        return "Error: Division by zero occurred."