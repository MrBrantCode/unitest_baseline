"""
QUESTION:
Write a Python function named `compare_demographics` that determines the best statistical method to use for comparing differences between diagnostic categories in demographics, considering nominal and ordinal variables. The function should take into account the type of variables, data distribution, and sample size when choosing the most suitable method.
"""

def compare_demographics(nominal_variables, ordinal_variables, data_distribution, sample_size):
    """
    Determine the best statistical method to use for comparing differences between diagnostic categories in demographics.

    Parameters:
    nominal_variables (list): List of nominal variables.
    ordinal_variables (list): List of ordinal variables.
    data_distribution (str): Distribution of the data (normal or non-normal).
    sample_size (int): Sample size.

    Returns:
    str: The most suitable statistical method.
    """

    if len(nominal_variables) > 0 and len(ordinal_variables) == 0:
        # If only nominal variables are present, use Chi-Square Test or Fisher's Exact Test
        if sample_size < 30:
            return "Fisher's Exact Test"
        else:
            return "Chi-Square Test"

    elif len(nominal_variables) == 0 and len(ordinal_variables) > 0:
        # If only ordinal variables are present, use ANOVA or Kruskal-Wallis H Test
        if data_distribution == "normal":
            return "One-way ANOVA"
        else:
            return "Kruskal-Wallis H Test"

    elif len(nominal_variables) > 0 and len(ordinal_variables) > 0:
        # If both nominal and ordinal variables are present, use Binary Logistic Regression
        return "Binary Logistic Regression"

    else:
        return "No variables provided"