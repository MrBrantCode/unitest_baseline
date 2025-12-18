"""
QUESTION:
Write a function named `calculate_bond_price_change` that takes in the initial yield curve, the bond's current price, the bond's duration, and the desired shock (interest rate change) to a specific maturity, and returns the new bond price after the shock. The yield curve is represented as a dictionary with maturities as keys and corresponding interest rates as values, and the shock is a tuple of (maturity, interest rate change). The function should account for non-parallel shifts in the yield curve.
"""

def calculate_bond_price_change(initial_yield_curve, current_price, duration, shock):
    """
    Calculate the new bond price after a shock to a specific maturity in the yield curve.

    Args:
        initial_yield_curve (dict): A dictionary with maturities as keys and corresponding interest rates as values.
        current_price (float): The bond's current price.
        duration (float): The bond's duration.
        shock (tuple): A tuple of (maturity, interest rate change).

    Returns:
        float: The new bond price after the shock.
    """
    # Assuming a non-parallel shift in the yield curve
    # We will calculate the change in yield for the specific maturity
    maturity, interest_rate_change = shock
    
    # Calculate the change in yield for the specific maturity
    new_yield = initial_yield_curve.get(maturity, 0) + interest_rate_change
    
    # Calculate the percentage change in yield
    percentage_change = (new_yield - initial_yield_curve.get(maturity, 0)) / (1 + initial_yield_curve.get(maturity, 0))
    
    # Calculate the new bond price using the duration
    new_price = current_price / (1 + duration * percentage_change)
    
    return new_price