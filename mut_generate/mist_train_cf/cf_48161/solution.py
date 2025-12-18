"""
QUESTION:
Write a function `attribute_pnl_to_greeks` that estimates the contribution of each Greek (Delta, Gamma, Theta, and Vega) to the Profit and Loss (P&L) of an European option given the entry and exit prices, and the values of the Greeks. The function should take as input the entry price, exit price, Delta, Gamma, Theta, Vega, change in time (in years), and change in volatility (as a decimal), and return a dictionary with the estimated contributions of each Greek to the P&L.
"""

def attribute_pnl_to_greeks(entry_price, exit_price, delta, gamma, theta, vega, time_change, volatility_change):
    """
    Estimates the contribution of each Greek to the P&L of an European option.

    Args:
        entry_price (float): The entry price of the option.
        exit_price (float): The exit price of the option.
        delta (float): The Delta value of the option.
        gamma (float): The Gamma value of the option.
        theta (float): The Theta value of the option.
        vega (float): The Vega value of the option.
        time_change (float): The change in time (in years).
        volatility_change (float): The change in volatility (as a decimal).

    Returns:
        dict: A dictionary with the estimated contributions of each Greek to the P&L.
    """

    price_change = exit_price - entry_price
    
    # Delta's contribution to P&L
    delta_contribution = price_change * delta

    # Gamma's contribution to P&L
    gamma_contribution = 0.5 * (price_change ** 2) * gamma

    # Theta's contribution to P&L
    theta_contribution = theta * time_change

    # Vega's contribution to P&L
    vega_contribution = vega * volatility_change

    # Total P&L
    total_pnl = delta_contribution + gamma_contribution - theta_contribution + vega_contribution

    # Calculate the percentage contributions of each Greek to the total P&L
    if total_pnl != 0:
        delta_percentage = (delta_contribution / total_pnl) * 100
        gamma_percentage = (gamma_contribution / total_pnl) * 100
        theta_percentage = (theta_contribution / total_pnl) * 100
        vega_percentage = (vega_contribution / total_pnl) * 100
    else:
        delta_percentage = 0
        gamma_percentage = 0
        theta_percentage = 0
        vega_percentage = 0

    # Return a dictionary with the estimated contributions of each Greek to the P&L
    return {
        'Delta': delta_contribution,
        'Gamma': gamma_contribution,
        'Theta': -theta_contribution, # Return the absolute value as it's a loss
        'Vega': vega_contribution,
        'Delta %': delta_percentage,
        'Gamma %': gamma_percentage,
        'Theta %': theta_percentage,
        'Vega %': vega_percentage
    }