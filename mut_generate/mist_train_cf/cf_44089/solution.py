"""
QUESTION:
Create a function `min_non_overlapping_periods` that takes a list of periods (where each period is a list of two integers representing the start and end of the period) as input and returns the smallest number of non-overlapping periods that cover the full range of the given periods. The function should also return the actual non-overlapping periods. The periods can be overlapping but not fully enveloping each other, and there could be several superior solutions. The function should use an efficient algorithm to handle these intricate scenarios.
"""

def min_non_overlapping_periods(periods):
    """
    This function takes a list of periods as input and returns the smallest number of non-overlapping periods 
    that cover the full range of the given periods. The function also returns the actual non-overlapping periods.

    Args:
        periods (list): A list of periods where each period is a list of two integers representing the start and end of the period.

    Returns:
        tuple: A tuple containing the smallest number of non-overlapping periods and the actual non-overlapping periods.
    """
    # Sort the periods in ascending order based on the end points
    periods.sort(key=lambda x: x[1])
    
    # Initialize the set of chosen periods with the first period
    chosen_periods = [periods[0]]
    
    # Iterate through the rest of the periods
    for period in periods[1:]:
        # If the current period does not intersect with the last one added to the set of chosen periods, add it to the set
        if period[0] >= chosen_periods[-1][1]:
            chosen_periods.append(period)
    
    # Return the smallest number of non-overlapping periods and the actual non-overlapping periods
    return len(chosen_periods), chosen_periods