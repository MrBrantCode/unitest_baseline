"""
QUESTION:
Write a function called `calculate_relative_effect_size` that takes as input the mean difference, the standard deviation for the control group, the standard deviation for the intervention group, the size of the control group, and the size of the intervention group. The function should return the relative effect size and its 95% confidence interval.
"""

import math

def calculate_relative_effect_size(mean_difference, sd_control, sd_intervention, n_control, n_intervention):
    """
    Calculate the relative effect size (standardized mean difference) and its 95% confidence interval.

    Args:
        mean_difference (float): The mean difference between the control and intervention groups.
        sd_control (float): The standard deviation of the control group.
        sd_intervention (float): The standard deviation of the intervention group.
        n_control (int): The size of the control group.
        n_intervention (int): The size of the intervention group.

    Returns:
        tuple: A tuple containing the relative effect size and its 95% confidence interval.
    """

    # Calculate the pooled standard deviation
    pooled_sd = math.sqrt(((n_control - 1) * sd_control ** 2 + (n_intervention - 1) * sd_intervention ** 2) / (n_control + n_intervention - 2))

    # Calculate the relative effect size (standardized mean difference)
    relative_effect_size = mean_difference / pooled_sd

    # Calculate the standard error
    standard_error = math.sqrt((sd_control ** 2 / n_control) + (sd_intervention ** 2 / n_intervention))

    # Calculate the 95% confidence interval
    ci_lower = relative_effect_size - 1.96 * standard_error
    ci_upper = relative_effect_size + 1.96 * standard_error

    return relative_effect_size, (ci_lower, ci_upper)