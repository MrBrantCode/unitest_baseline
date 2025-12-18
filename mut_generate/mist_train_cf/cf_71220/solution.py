"""
QUESTION:
Write a function called `capture_interaction` that explains how non-linear models capture the interaction between two variables, including the limitation of linear models in this regard.
"""

def capture_interaction(X1, X2, model_type='linear'):
    """
    This function simulates how non-linear models capture the interaction between two variables.
    
    Args:
    X1 (list): The first independent variable.
    X2 (list): The second independent variable.
    model_type (str, optional): The type of model. Defaults to 'linear'.
    
    Returns:
    str: A description of how the interaction is captured by the model.
    """

    if model_type == 'linear':
        return "Linear models assume a linear relationship between variables and cannot capture complex interactions."
    elif model_type == 'non-linear':
        return "Non-linear models can capture complex relationships or interactions between variables by considering higher degree and interaction terms."
    else:
        return "Unsupported model type."