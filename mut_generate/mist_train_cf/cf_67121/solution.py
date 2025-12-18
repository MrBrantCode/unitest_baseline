"""
QUESTION:
The function `regularisation_impact` is used to analyze the impact of the regularization parameter λ on the testing error in a least-squares regression model. Given the regularization parameter λ, write the function `regularisation_impact` to describe its effect on the testing error. Assume the model's optimization is executed exactly and consider the relationship between λ and testing error to be U-shaped.
"""

def regularisation_impact(regularization_parameter):
    """
    Analyzes the impact of the regularization parameter λ on the testing error in a least-squares regression model.

    The function assumes the model's optimization is executed exactly and considers the relationship between λ and testing error to be U-shaped.

    Args:
        regularization_parameter (float): The regularization parameter λ.

    Returns:
        str: A description of the effect of the regularization parameter on the testing error.
    """
    if regularization_parameter < 0:
        return "Error: The regularization parameter λ should be a non-negative number."
    elif regularization_parameter == 0:
        return "The model may overfit the training data, resulting in a high testing error."
    elif regularization_parameter > 0 and regularization_parameter < 1:
        return "The model's complexity is reduced, and the testing error may decrease."
    else:
        return "The model becomes too simple and may underfit the training data, resulting in a high testing error."