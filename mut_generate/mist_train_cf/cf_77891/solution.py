"""
QUESTION:
Create a function called `calculate_cds_spread` to normalize the notional values of underlying bonds in constructing a term structure of CDS spread from an issuer. The function should take into account the standardization of CDS spreads for contract sizes, typically $10 million notional, and the variation of CDS spreads with different maturities.
"""

def calculate_cds_spread(contract_size: float, annual_spread: float, maturity: float) -> float:
    """
    Calculates the CDS spread for a given contract size, annual spread, and maturity.

    Args:
        contract_size (float): The size of the CDS contract, typically $10 million notional.
        annual_spread (float): The annual amount (in basis points) that a protection buyer pays to a protection seller.
        maturity (float): The maturity of the CDS contract in years.

    Returns:
        float: The calculated CDS spread.
    """

    # Calculate the CDS spread
    cds_spread = (annual_spread / 100) * contract_size * maturity

    return cds_spread