"""
QUESTION:
Write a function `calculate_portfolio_risk_and_return` that calculates the portfolio return and risk for two securities A and B given their expected returns, risks (standard deviations), and the correlation coefficient between them. The function should take the expected returns of A and B, their standard deviations, the correlation coefficient, and the weights of A and B as input, and return the portfolio return and risk (standard deviation). The portfolio return should be calculated as the sum of the product of the proportion of total investment in each security and their respective expected returns, and the portfolio risk should be calculated as the square root of the portfolio variance, which is calculated using the formula Var(P) = w1^2 * σ1^2 + w2^2 * σ2^2 + 2 * ρ * σ1 * σ2 * w1 * w2. 

Assume that the weights of A and B add up to 1, and the correlation coefficient is a value between -1 and 1. The expected returns and standard deviations should be given as decimal values (e.g., 12% should be given as 0.12).
"""

def calculate_portfolio_risk_and_return(expected_return_A, expected_return_B, std_dev_A, std_dev_B, correlation_coefficient, weight_A, weight_B):
    """
    Calculate the portfolio return and risk for two securities A and B.

    Args:
        expected_return_A (float): Expected return of security A.
        expected_return_B (float): Expected return of security B.
        std_dev_A (float): Standard deviation of security A.
        std_dev_B (float): Standard deviation of security B.
        correlation_coefficient (float): Correlation coefficient between the two securities.
        weight_A (float): Weight of security A in the portfolio.
        weight_B (float): Weight of security B in the portfolio.

    Returns:
        tuple: A tuple containing the portfolio return and risk.
    """
    # Calculate portfolio return
    portfolio_return = weight_A * expected_return_A + weight_B * expected_return_B
    
    # Calculate portfolio variance
    portfolio_variance = (weight_A ** 2) * (std_dev_A ** 2) + (weight_B ** 2) * (std_dev_B ** 2) + 2 * correlation_coefficient * std_dev_A * std_dev_B * weight_A * weight_B
    
    # Calculate portfolio risk (standard deviation)
    portfolio_risk = portfolio_variance ** 0.5
    
    return portfolio_return, portfolio_risk