"""
QUESTION:
Write a function called `report_bayesian_regression_results` that reports the results of Bayesian regression in academic papers, specifically focusing on how to properly report the 95% credible intervals for the point estimates of the model parameters. Ensure the function clarifies the difference between credible intervals and confidence intervals, as well as the distinction between Bayesian and frequentist approaches.
"""

def report_bayesian_regression_results(point_estimate, lower_ci, upper_ci):
    """
    Reports the results of Bayesian regression.

    Args:
        point_estimate (float): The point estimate of the model parameter.
        lower_ci (float): The lower bound of the 95% credible interval.
        upper_ci (float): The upper bound of the 95% credible interval.

    Returns:
        str: A string reporting the results of Bayesian regression.
    """

    return f"The point estimate is {point_estimate} with a 95% credible interval of ({lower_ci}; {upper_ci}). The reported credible interval represents the range within which the true parameter value lies with a 95% probability based on our posterior distribution."