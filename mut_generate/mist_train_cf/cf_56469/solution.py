"""
QUESTION:
Write a function `select_model` that takes in the residuals of the zero-knot, one-knot, and two-knot linear spline models fitted with robust linear regressions, specifically with Huber estimations, and returns the best model based on a suitable criterion for model selection. The function should also be able to compare models fitted with different robust regression techniques, such as Huber regression and Tukey's bisquare estimation.
"""

def select_model(zero_knot_residuals, one_knot_residuals, two_knot_residuals):
    """
    This function selects the best model based on the sum of squared errors (SSE) of the residuals.

    Parameters:
    zero_knot_residuals (list): Residuals of the zero-knot linear spline model.
    one_knot_residuals (list): Residuals of the one-knot linear spline model.
    two_knot_residuals (list): Residuals of the two-knot linear spline model.

    Returns:
    str: The name of the best model.
    """
    # Calculate the sum of squared errors for each model
    zero_knot_sse = sum([x**2 for x in zero_knot_residuals])
    one_knot_sse = sum([x**2 for x in one_knot_residuals])
    two_knot_sse = sum([x**2 for x in two_knot_residuals])

    # Compare the SSE of each model and return the best one
    min_sse = min(zero_knot_sse, one_knot_sse, two_knot_sse)
    if min_sse == zero_knot_sse:
        return "Zero-knot model"
    elif min_sse == one_knot_sse:
        return "One-knot model"
    else:
        return "Two-knot model"