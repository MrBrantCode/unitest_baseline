"""
QUESTION:
Write a function called `interpolate_yield_rate` that calculates the yield rate for a given maturity by interpolating between two known yield rates of U.S. Treasury bonds with durations closest to the option's time to maturity. Assume the function takes three arguments: `lower_duration`, `lower_yield`, `upper_duration`, and `upper_yield`, representing the durations and corresponding yields of the two Treasury bonds, and `maturity`, representing the option's time to maturity. The function should return the interpolated yield rate for the given maturity.
"""

def interpolate_yield_rate(lower_duration, lower_yield, upper_duration, upper_yield, maturity):
    """
    This function calculates the yield rate for a given maturity by interpolating 
    between two known yield rates of U.S. Treasury bonds with durations closest to 
    the option's time to maturity.

    Args:
        lower_duration (float): The duration of the lower Treasury bond.
        lower_yield (float): The yield of the lower Treasury bond.
        upper_duration (float): The duration of the upper Treasury bond.
        upper_yield (float): The yield of the upper Treasury bond.
        maturity (float): The option's time to maturity.

    Returns:
        float: The interpolated yield rate for the given maturity.
    """

    # Calculate the interpolated yield rate using linear interpolation
    return lower_yield + (upper_yield - lower_yield) * (maturity - lower_duration) / (upper_duration - lower_duration)