"""
QUESTION:
Write a function called `compare_model_selection_criteria` that compares the Schwarz Bayesian Criterion (SBC) and Hannan-Quinn Information Criterion (HQIC) in terms of their complexity penalties. The function should take in the number of parameters (p) and the sample size (n) as inputs, and return a string describing how the SBC and HQIC might be biased based on these values.

Note that the function does not need to calculate the actual SBC and HQIC values, but rather provide a qualitative description of their biases. Assume that the true model is complex if the number of parameters (p) is greater than 5, and the sample size (n) is considered small if it is less than 100.
"""

def compare_model_selection_criteria(p, n):
    """
    Compare the Schwarz Bayesian Criterion (SBC) and Hannan-Quinn Information Criterion (HQIC) 
    in terms of their complexity penalties based on the number of parameters (p) and the sample size (n).

    Args:
        p (int): The number of parameters.
        n (int): The sample size.

    Returns:
        str: A string describing how the SBC and HQIC might be biased based on the input values.
    """

    # Determine if the true model is complex
    complex_model = p > 5
    
    # Determine if the sample size is small
    small_sample = n < 100

    # If the model is complex, SBC might over-simplify and HQIC might overfit
    if complex_model:
        return "SBC might be biased towards over-simplification, leading to underfitting, while HQIC might be biased towards overfitting."
    
    # If the sample size is small, HQIC might overfit and SBC might be more robust
    elif small_sample:
        return "HQIC might be biased towards overfitting, while SBC might be more robust due to its heavier penalty for model complexity."
    
    # If neither condition is met, both criteria should perform well
    else:
        return "Both SBC and HQIC should perform well, with SBC possibly being more computationally efficient."