"""
QUESTION:
Write a function named `calculate_discount_rate` that takes in a risk aversion level and expected return as parameters. This function should return the discount rate for a risk-averse individual based on the given risk aversion level and expected return. Assume a direct relationship between the risk aversion level and discount rate, and the discount rate is calculated as the product of the risk aversion level and expected return. The risk aversion level and expected return are both positive float numbers, and the function should return a float number.
"""

def calculate_discount_rate(risk_aversion_level, expected_return):
    """
    Calculate the discount rate for a risk-averse individual.

    Args:
    risk_aversion_level (float): The level of risk aversion.
    expected_return (float): The expected return.

    Returns:
    float: The calculated discount rate.
    """
    # Assuming a direct relationship between risk aversion level and discount rate,
    # the discount rate is calculated as the product of the risk aversion level and expected return.
    return risk_aversion_level * expected_return