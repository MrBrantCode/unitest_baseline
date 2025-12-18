"""
QUESTION:
Write a function `calculate_gain` that calculates the gain for a given set of values. The function should take in the following parameters: `GL`, `GR`, `HL`, `HR`, `lambda_val`, and `gamma`, and return the calculated gain value. The gain should be calculated using the formula: 

Gain = 0.5 * ((GL^2 / (HL + lambda_val)) + (GR^2 / (HR + lambda_val)) - ((GL + GR)^2 / (HL + HR + lambda_val))) - gamma 

Restrictions: The function should be a Python function, and should not take any other parameters than the specified ones.
"""

def calculate_gain(GL, GR, HL, HR, lambda_val, gamma):
    """
    Calculate the gain for a given set of values.

    Parameters:
    GL (float): First gradient value for the left child
    GR (float): First gradient value for the right child
    HL (float): Second gradient value for the left child
    HR (float): Second gradient value for the right child
    lambda_val (float): Regularization parameter
    gamma (float): Gamma value

    Returns:
    float: Calculated gain value
    """
    return 0.5 * ((GL**2 / (HL + lambda_val)) + (GR**2 / (HR + lambda_val)) - ((GL + GR)**2 / (HL + HR + lambda_val))) - gamma