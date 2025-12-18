"""
QUESTION:
Write a function named `calculate_funding_benefit` to calculate the funding benefit of equity. This function should take into account the institution's cost of capital, risk profile, or other internal metrics such as weighted average cost of capital (WACC), risk-free rate, market risk premium, and the institution's own beta (systematic risk).
"""

def calculate_funding_benefit(wacc, risk_free_rate, market_risk_premium, beta):
    """
    Calculate the funding benefit of equity based on the institution's cost of capital, 
    risk profile, or other internal metrics.

    Parameters:
    wacc (float): Weighted average cost of capital
    risk_free_rate (float): Risk-free rate
    market_risk_premium (float): Market risk premium
    beta (float): Institution's beta (systematic risk)

    Returns:
    float: Funding benefit of equity
    """
    # Calculate the funding benefit using the given parameters
    # For simplicity, let's assume the funding benefit is a function of WACC and beta
    funding_benefit = wacc / (1 + beta * market_risk_premium - risk_free_rate)
    return funding_benefit