"""
QUESTION:
Given a linear regression model where ln(wage) = β0 + β1educ + β2educ*college, with the variable college defined as 1 if educ ≥ 16 and 0 otherwise, write a function `estimated_impact` that calculates the following: 

1. the estimated impact of educ on wage for non-college graduates 
2. the estimated impact of educ on wage for college graduates 
3. whether there is evidence that the impacts for the two groups are different.

Assume the regression coefficients β0, β1, and β2 are given. The function should return the results for the three queries.
"""

def estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2):
    """
    Calculate the estimated impact of education on wage for non-college and college graduates,
    and determine if the impacts are significantly different.

    Parameters:
    - beta0 (float): Intercept of the linear regression model
    - beta1 (float): Coefficient of educ in the linear regression model
    - beta2 (float): Coefficient of educ*college in the linear regression model
    - std_err_beta2 (float): Standard error of beta2
    - p_value_beta2 (float): P-value of beta2

    Returns:
    - impact_non_college (float): Estimated impact of educ on wage for non-college graduates
    - impact_college (float): Estimated impact of educ on wage for college graduates
    - is_impact_different (bool): Whether the impacts for the two groups are significantly different
    """

    # Estimated impact of educ on wage for non-college graduates
    impact_non_college = beta1

    # Estimated impact of educ on wage for college graduates
    impact_college = beta1 + beta2

    # Check if the impact is significantly different for the two groups
    # Assuming a significance level of 0.05
    is_impact_different = p_value_beta2 < 0.05

    return impact_non_college, impact_college, is_impact_different