"""
QUESTION:
Write a function `calculate_picp_pinaw` that calculates the Prediction Interval Coverage Probability (PICP) and Prediction Interval Normalized Average Width (PINAW) for evaluating the accuracy of prediction intervals in a time series data. 

The function should take in the following parameters: 
- `lower_bounds`: a list of lower bounds of prediction intervals
- `upper_bounds`: a list of upper bounds of prediction intervals
- `actual_values`: a list of actual observations

The function should return a tuple of PICP and PINAW values. The PICP is the proportion of actual observations that fall within the prediction interval and the PINAW is the average prediction interval width normalized to the range of observed values.
"""

def calculate_picp_pinaw(lower_bounds, upper_bounds, actual_values):
    """
    Calculate the Prediction Interval Coverage Probability (PICP) and 
    Prediction Interval Normalized Average Width (PINAW) for evaluating 
    the accuracy of prediction intervals in a time series data.

    Args:
    - lower_bounds (list): A list of lower bounds of prediction intervals
    - upper_bounds (list): A list of upper bounds of prediction intervals
    - actual_values (list): A list of actual observations

    Returns:
    - tuple: A tuple containing the PICP and PINAW values
    """

    # Calculate PICP
    within_interval = [1 if lower <= actual <= upper else 0 
                       for lower, upper, actual in zip(lower_bounds, upper_bounds, actual_values)]
    picp = sum(within_interval) / len(within_interval)

    # Calculate PINAW
    interval_widths = [upper - lower for lower, upper in zip(lower_bounds, upper_bounds)]
    actual_range = max(actual_values) - min(actual_values)
    pinaw = sum(interval_widths) / (actual_range * len(interval_widths))

    return picp, pinaw