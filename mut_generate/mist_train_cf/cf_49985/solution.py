"""
QUESTION:
Transform the Dupire formula's denominator for a discrete implied volatility grid, where the denominator contains derivatives that are not directly applicable. Create a function named `check_dupire_denominator_discrete` that checks if the discretized denominator remains positive everywhere on the grid. Implement the function using finite differences to approximate the derivatives. The input to the function should include the discrete set of implied volatilities and corresponding strike prices for a certain maturity T.
"""

def check_dupire_denominator_discrete(implied_volatilities, strike_prices):
    """
    Check if the discretized Dupire formula's denominator remains positive everywhere on the grid.

    Parameters:
    implied_volatilities (list): A list of discrete implied volatilities.
    strike_prices (list): A list of corresponding strike prices.

    Returns:
    bool: True if the discretized denominator is positive everywhere, False otherwise.
    """
    
    # Calculate the differences in strike prices
    delta_K = [strike_prices[i+1] - strike_prices[i] for i in range(len(strike_prices) - 1)]
    
    # Calculate the first derivative using forward difference
    first_derivative = [(implied_volatilities[i+1]**2 - implied_volatilities[i]**2) / delta_K[i] for i in range(len(implied_volatilities) - 1)]
    
    # Calculate the second derivative using forward difference
    second_derivative = [(implied_volatilities[i+2]**2 - 2*implied_volatilities[i+1]**2 + implied_volatilities[i]**2) / (delta_K[i] * delta_K[i+1]) for i in range(len(implied_volatilities) - 2)]
    
    # Calculate the Dupire formula's denominator
    denominator = [1 - 2 * (strike_prices[i+1] * first_derivative[i]) / (implied_volatilities[i+1]**2) + (strike_prices[i+1]**2 / implied_volatilities[i+1]**2) * second_derivative[i] for i in range(len(implied_volatilities) - 2)]
    
    # Check if the denominator is positive everywhere
    return all(d > 0 for d in denominator)