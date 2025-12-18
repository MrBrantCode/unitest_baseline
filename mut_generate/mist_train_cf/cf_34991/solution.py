"""
QUESTION:
Implement a Python class called `WeightedAverageCalculator` to calculate the weighted average of a set of indicators. The class should have a constructor that accepts a `group_factor` as a parameter and a method `add_indicator` to add an indicator object. The class should also have a method `calculate_weighted_average` that returns the weighted average of all added indicators. The weighted average is calculated by multiplying each indicator's factor by the group factor, summing these values, and then dividing by the total number of indicators.
"""

def weighted_average(indicators, group_factor):
    """
    Calculate the weighted average of a set of indicators.

    Args:
    indicators (list): A list of dictionaries, each containing 'factor' key.
    group_factor (float): The group factor to apply to each indicator's factor.

    Returns:
    float: The weighted average of the indicators.
    """
    total_weighted_sum = sum(indicator['factor'] * group_factor for indicator in indicators)
    weighted_average = total_weighted_sum / len(indicators)
    return weighted_average