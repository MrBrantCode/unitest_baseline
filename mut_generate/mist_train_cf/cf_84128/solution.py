"""
QUESTION:
Write a function `estimate_bond_yield_change` that estimates the change in 10-year bond yield based on the change in policy rate and other macroeconomic factors using multiple regression. The function should take in the following parameters: 
- `policy_rate_change`: the change in policy rate
- `gdp_change`: the change in GDP
- `inflation_change`: the change in inflation
- `unemployment_change`: the change in unemployment
- `fiscal_deficit_change`: the change in fiscal deficit
- `beta_coefficients`: a list or tuple of beta coefficients (β0, β1, β2, β3, β4, β5) from the multiple regression model
The function should return the estimated change in 10-year bond yield.
"""

def estimate_bond_yield_change(policy_rate_change, gdp_change, inflation_change, unemployment_change, fiscal_deficit_change, beta_coefficients):
    """
    Estimates the change in 10-year bond yield based on the change in policy rate and other macroeconomic factors using multiple regression.

    Args:
        policy_rate_change (float): The change in policy rate
        gdp_change (float): The change in GDP
        inflation_change (float): The change in inflation
        unemployment_change (float): The change in unemployment
        fiscal_deficit_change (float): The change in fiscal deficit
        beta_coefficients (list or tuple): A list or tuple of beta coefficients (β0, β1, β2, β3, β4, β5) from the multiple regression model

    Returns:
        float: The estimated change in 10-year bond yield
    """
    # Unpack beta coefficients
    beta_0, beta_1, beta_2, beta_3, beta_4, beta_5 = beta_coefficients
    
    # Calculate the estimated change in 10-year bond yield using the multiple regression model
    estimated_change = beta_0 + beta_1 * policy_rate_change + beta_2 * gdp_change + beta_3 * inflation_change + beta_4 * unemployment_change + beta_5 * fiscal_deficit_change
    
    return estimated_change