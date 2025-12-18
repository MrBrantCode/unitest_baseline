"""
QUESTION:
Write a function called `compare_aic_bic_bias` that compares and contrasts the intrinsic biases of the Bayesian Information Criterion (BIC) and the Akaike Information Criterion (AIC) in statistical model selection methodologies. The function should provide conditions or occurrences that provoke discrepancies between the two criteria's selected models, but it should not include any implementation details of AIC and BIC calculations.
"""

def compare_aic_bic_bias(model_complexity, overfitting_concern):
    """
    Compares the intrinsic biases of AIC and BIC in model selection methodologies.
    
    Args:
    model_complexity (str): 'simple' or 'complex'
    overfitting_concern (bool): True if overfitting is a concern
    
    Returns:
    str: A message describing the preferred criterion based on model complexity and overfitting concern
    """

    if model_complexity == 'complex' and not overfitting_concern:
        return "AIC may perform better in this scenario."
    elif model_complexity == 'simple' or overfitting_concern:
        return "BIC may excel in this scenario."
    else:
        return "The choice of criterion depends on the specific characteristics and requirements of the data and modeling problem."