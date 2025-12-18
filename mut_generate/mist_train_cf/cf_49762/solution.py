"""
QUESTION:
Write a function called `build_cross_currency_funding_curve` that constructs a cross-currency funding curve given market data inputs. The function should take into account the risk-free discount curve in the payment currency, the spread between unsecured and secured funding rates in the payment currency, foreign exchange forward rates to convert the curve to the collateral currency, and the funding cost of the collateral currency. The function should return the resultant curve representing the time value of money in the payment currency, adjusted for the cost of sourcing collateral in the collateral currency.
"""

def build_cross_currency_funding_curve(risk_free_discount_curve, 
                                      unsecured_secured_spread, 
                                      foreign_exchange_forward_rates, 
                                      collateral_funding_cost):
    """
    Construct a cross-currency funding curve given market data inputs.

    Parameters:
    risk_free_discount_curve (dict): The risk-free discount curve in the payment currency.
    unsecured_secured_spread (float): The spread between unsecured and secured funding rates in the payment currency.
    foreign_exchange_forward_rates (dict): Foreign exchange forward rates to convert the curve to the collateral currency.
    collateral_funding_cost (float): The funding cost of the collateral currency.

    Returns:
    dict: The resultant curve representing the time value of money in the payment currency, 
          adjusted for the cost of sourcing collateral in the collateral currency.
    """

    # Apply the spread to the risk-free discount curve
    adjusted_curve = {tenor: rate + unsecured_secured_spread for tenor, rate in risk_free_discount_curve.items()}

    # Convert to the collateral currency using the foreign exchange forward rates
    converted_curve = {tenor: rate * foreign_exchange_forward_rates[tenor] for tenor, rate in adjusted_curve.items()}

    # Adjust the converted curve by the funding cost of the collateral currency
    cross_currency_curve = {tenor: rate + collateral_funding_cost for tenor, rate in converted_curve.items()}

    return cross_currency_curve