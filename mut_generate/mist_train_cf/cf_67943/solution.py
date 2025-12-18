"""
QUESTION:
Given a hypothesis test with null hypothesis H0: p = 0.6, alternative hypothesis Ha: p = 0.7, and power of the test equal to 0.8, determine the correct conclusions that can be drawn from the results.
"""

def calculate_type_II_error(power):
    """
    Calculate the probability of making a Type II error given the power of the test.

    Args:
    power (float): The power of the test.

    Returns:
    float: The probability of making a Type II error.
    """
    return 1 - power

# Example usage
power = 0.8
type_II_error = calculate_type_II_error(power)
print("The probability of making a Type II error is:", type_II_error)