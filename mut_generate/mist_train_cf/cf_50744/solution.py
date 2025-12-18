"""
QUESTION:
You have a correlation matrix and want to identify the variables that lead to the greatest increase in another variable of interest, 'retention'. However, when you look at the highest correlated variable 'income' with 'retention', the highest income cities do not have the highest 'retention'. Write a function named `identify_influential_variables` to help identify the influential variables.
"""

def identify_influential_variables(correlation_matrix, target_variable):
    """
    Identify the variables that lead to the greatest increase in the target variable.

    Parameters:
    correlation_matrix (pandas DataFrame): A correlation matrix.
    target_variable (str): The target variable of interest.

    Returns:
    list: A list of influential variables sorted by their absolute correlation with the target variable.
    """
    # Get the correlations with the target variable
    correlations = correlation_matrix[target_variable].drop(target_variable)

    # Sort the correlations by absolute value in descending order
    correlations = correlations.reindex(correlations.abs().sort_values(ascending=False).index)

    # Return the influential variables
    return correlations.index.tolist()