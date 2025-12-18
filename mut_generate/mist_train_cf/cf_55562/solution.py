"""
QUESTION:
Write a function called `wilcoxon_test_interpreter` that takes in two parameters: `male_values` and `female_values`, representing the dwelling problems safety values for males and females, respectively. The function should return a string stating which gender has more effect on dwelling problems safety based on their median values.
"""

import numpy as np

def wilcoxon_test_interpreter(male_values, female_values):
    """
    This function determines which gender has more effect on dwelling problems safety based on their median values.

    Parameters:
    male_values (list): A list of dwelling problems safety values for males.
    female_values (list): A list of dwelling problems safety values for females.

    Returns:
    str: A string stating which gender has more effect on dwelling problems safety.
    """

    # Calculate the median of male and female values
    median_male = np.median(male_values)
    median_female = np.median(female_values)

    # Compare the medians to determine which gender has more effect
    if median_male > median_female:
        return "Males have more effect on dwelling problems safety."
    elif median_female > median_male:
        return "Females have more effect on dwelling problems safety."
    else:
        return "Both males and females have the same effect on dwelling problems safety."