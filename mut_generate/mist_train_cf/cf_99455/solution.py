"""
QUESTION:
Write a function called `calculate_subsidized_farmers` that calculates the percentage of vegetable farmers who received government subsidies given the total number of vegetable farmers surveyed and the number of farmers who reported struggling with increasing production costs. The result should be rounded to the nearest whole number.
"""

def calculate_subsidized_farmers(total_farmers, struggling_farmers):
    """
    Calculate the percentage of vegetable farmers who received government subsidies.

    Args:
    total_farmers (int): Total number of vegetable farmers surveyed.
    struggling_farmers (int): Number of farmers who reported struggling with increasing production costs.

    Returns:
    int: Percentage of vegetable farmers who received government subsidies, rounded to the nearest whole number.
    """
    percentage_subsidized = (struggling_farmers / total_farmers) * 100
    return round(percentage_subsidized)