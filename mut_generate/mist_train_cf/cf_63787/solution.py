"""
QUESTION:
Write a Python function `adjust_p_values` that determines whether p-values need to be adjusted for multiple univariate analyses before running a multiple regression. The function should consider the context of the analysis (exploratory or confirmatory) and the field of study (e.g., medical).
"""

def adjust_p_values(context, field, p_values):
    """
    Determine whether p-values need to be adjusted for multiple univariate analyses before running a multiple regression.

    Args:
    context (str): The context of the analysis (exploratory or confirmatory)
    field (str): The field of study (e.g., medical)
    p_values (list): A list of p-values from univariate analyses

    Returns:
    list: Adjusted p-values if necessary, otherwise the original p-values
    """

    # In this case, we assume that we will not adjust p-values for exploratory analysis
    # and we will use Bonferroni correction for confirmatory analysis in the medical field
    if context == 'exploratory':
        return p_values
    elif context == 'confirmatory' and field == 'medical':
        import numpy as np
        # Apply Bonferroni correction
        adjusted_p_values = np.multiply(p_values, len(p_values))
        # Ensure adjusted p-values do not exceed 1
        adjusted_p_values = np.minimum(adjusted_p_values, 1)
        return adjusted_p_values
    else:
        # For other contexts or fields, we do not adjust p-values
        return p_values