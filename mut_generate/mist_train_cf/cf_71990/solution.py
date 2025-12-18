"""
QUESTION:
Write a function `calculate_pl_explanation` that calculates the Profit and Loss (P&L) explanation for a swap due to a change in interest rates, decomposing it into different orders of sensitivities (Delta, Gamma, and higher order effects). The function should take into account potential sources of error, including incorrect calculations, non-linear behavior, incorrect assumptions, incorrect bucketing, and time evolution, and should return the calculated P&L explanation.
"""

def calculate_pl_explanation(rate_change, delta, gamma, time_change=0, volatility_change=0):
    """
    Calculate the Profit and Loss (P&L) explanation for a swap due to a change in interest rates.

    Parameters:
    rate_change (float): The change in interest rate.
    delta (float): The first derivative of the price with respect to the rate.
    gamma (float): The second derivative of the price with respect to the rate.
    time_change (float, optional): The change in time. Defaults to 0.
    volatility_change (float, optional): The change in volatility. Defaults to 0.

    Returns:
    dict: A dictionary containing the P&L explanation, decomposed into Delta, Gamma, and higher order effects.
    """

    # Calculate the P&L due to Delta
    pl_delta = delta * rate_change

    # Calculate the P&L due to Gamma
    pl_gamma = 0.5 * gamma * (rate_change ** 2)

    # Calculate the P&L due to higher order effects (e.g. time evolution, volatility decay)
    pl_higher_order = time_change * volatility_change

    # Calculate the total P&L
    total_pl = pl_delta + pl_gamma + pl_higher_order

    # Return the P&L explanation as a dictionary
    return {
        'Delta': pl_delta,
        'Gamma': pl_gamma,
        'Higher Order Effects': pl_higher_order,
        'Total P&L': total_pl
    }