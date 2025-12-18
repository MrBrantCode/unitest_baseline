"""
QUESTION:
Write a function called `calculate_dv01` that calculates the dollar value of a basis point (DV01) for a portfolio of SOFR futures contracts. The function should take as input a list of dictionaries, where each dictionary represents a futures contract and contains the keys 'duration', 'notional_amount', and 'change_in_yield'. The function should return the total DV01 for the portfolio.
"""

def calculate_dv01(portfolio):
    """
    Calculate the total dollar value of a basis point (DV01) for a portfolio of SOFR futures contracts.

    Args:
    portfolio (list): A list of dictionaries, where each dictionary represents a futures contract and contains the keys 'duration', 'notional_amount', and 'change_in_yield'.

    Returns:
    float: The total DV01 for the portfolio.
    """
    total_dv01 = 0
    for contract in portfolio:
        # Calculate the DV01 for the current contract
        contract_dv01 = contract['duration'] * contract['notional_amount'] * contract['change_in_yield']
        # Add the contract's DV01 to the total
        total_dv01 += contract_dv01
    return total_dv01