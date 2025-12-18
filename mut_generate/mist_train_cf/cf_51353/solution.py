"""
QUESTION:
Write a function `is_perfect_fit_necessary` that determines if a perfect fit to the vanilla skew is necessary for a given portfolio of derivatives. The function should take into account the type of products in the portfolio and their exposure to forward start or future implied volatility.
"""

def is_perfect_fit_necessary(portfolio):
    """
    Determines if a perfect fit to the vanilla skew is necessary for a given portfolio of derivatives.
    
    Args:
    portfolio (list): A list of dictionaries containing information about each product in the portfolio.
                      Each dictionary should have the keys 'type' and 'exposure'.
    
    Returns:
    bool: True if a perfect fit to the vanilla skew is necessary, False otherwise.
    """

    # Check if the portfolio contains any vanilla options or products that can be replicated by vanillas
    if any(product['type'] in ['vanilla', 'replicable'] for product in portfolio):
        return True
    
    # If the portfolio contains exotic products, check their exposure to forward start or future implied volatility
    for product in portfolio:
        if product['type'] == 'exotic' and product['exposure'] in ['forward_start', 'future_implied']:
            # If an exotic product has exposure to forward start or future implied volatility, a perfect fit is not necessary
            return False
    
    # If the portfolio only contains exotic products with no exposure to forward start or future implied volatility, a perfect fit is necessary
    return True