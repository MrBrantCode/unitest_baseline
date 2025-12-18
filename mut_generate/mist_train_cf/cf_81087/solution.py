"""
QUESTION:
Write a function `nested_model` that determines whether a given linear mixed effects model is a nested or crossed model. The model should have a fixed effect of language nested in each region of interest (ROI), and include random effects of subjects and other covariates. 

The model should be in the form of `lmer(FCM ~ ROI_Pair * language + cov_1 + cov_2 + (1|subject), data = df)`, where `FCM` is the dependent variable, `ROI_Pair` and `language` are the fixed effects, `cov_1` and `cov_2` are covariates, and `subject` is the random effect. 

Assume that the language is nested within each ROI_Pair, meaning that for each ROI_Pair, there are different levels of language. The function should return a string indicating whether the model is nested or crossed, and whether it is appropriate for the given data structure.
"""

def nested_model(model_equation):
    """
    Determine whether a given linear mixed effects model is nested or crossed.

    Args:
    model_equation (str): A string representing the model equation in R's lmer syntax.

    Returns:
    str: A string indicating whether the model is nested or crossed.
    """
    # Check if the model equation includes an interaction term between ROI_Pair and language
    if "* language" in model_equation and "(1|subject)" in model_equation:
        return "The model is a nested mixed effects model."
    else:
        return "The model is not a nested mixed effects model."