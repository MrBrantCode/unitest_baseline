"""
QUESTION:
Write a function `convert_cohen_f_to_eta_square` that calculates eta-square from a given Cohen's f in a 2x2 Mixed ANOVA, considering that the transformation formula for between-subject effects is not directly applicable in this context. The function should take Cohen's f as input and return the calculated eta-square value. Note that the function should acknowledge that the conversion may not be accurate due to different assumptions and interpretations in mixed-model contexts.
"""

def convert_cohen_f_to_eta_square(cohens_f):
    """
    This function calculates eta-square from a given Cohen's f in a 2x2 Mixed ANOVA.
    
    Note: The conversion may not be accurate due to different assumptions and interpretations in mixed-model contexts.
    
    Parameters:
    cohens_f (float): Cohen's f value
    
    Returns:
    float: The calculated eta-square value
    """
    eta_square = cohens_f**2 / (1 + cohens_f**2)
    return eta_square