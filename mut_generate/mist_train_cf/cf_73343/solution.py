"""
QUESTION:
Write a function named `evaluate_survey_design` that assesses the design quality of a survey. The function should consider aspects such as the usage of chance in sampling, response rate, potential presence of selection bias, or the tendency for a voluntary response study to potentially skew towards those with strongly held views.
"""

def evaluate_survey_design(sampling_method, response_rate, selection_bias, voluntary_bias):
    """
    This function evaluates the design quality of a survey.

    Args:
    sampling_method (str): The method used for sampling (e.g., simple random sample, non-probability sampling).
    response_rate (float): The percentage of participants who responded to the survey.
    selection_bias (bool): Whether the survey suffers from selection bias.
    voluntary_bias (bool): Whether the survey is affected by voluntary response bias.

    Returns:
    str: A message assessing the design quality of the survey.
    """

    design_quality = ""

    if sampling_method == "simple random sample":
        design_quality += "The sampling method used is generally good, but "
    else:
        design_quality += "The sampling method used may be a concern, as it "

    if selection_bias:
        design_quality += "may not adequately represent the diversity of the entire population, which could lead to selection bias. "
    else:
        design_quality += "adequately represents the diversity of the entire population. "

    if response_rate > 90:
        design_quality += "The response rate is high, which may help reduce non-response bias. "
    else:
        design_quality += "The response rate could be improved to reduce non-response bias. "

    if voluntary_bias:
        design_quality += "The survey may be affected by voluntary response bias, which could skew towards those with strongly-held views."
    else:
        design_quality += "The survey does not appear to be significantly affected by voluntary response bias."

    return design_quality