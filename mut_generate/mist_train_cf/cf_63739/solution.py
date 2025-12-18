"""
QUESTION:
Write a function `eurodollar_futures_settlement_price` to calculate the Eurodollar futures settlement price given the LIBOR rate. The function should take one argument `libor_rate` which is the LIBOR rate at expiration as a decimal. The function should return the settlement price of the Eurodollar futures contract. The settlement price should be calculated using the standard convention of $100 - LIBOR$ and the result should be a float value.
"""

def eurodollar_futures_settlement_price(libor_rate):
    """
    Calculate the Eurodollar futures settlement price given the LIBOR rate.

    Args:
        libor_rate (float): The LIBOR rate at expiration as a decimal.

    Returns:
        float: The settlement price of the Eurodollar futures contract.
    """
    return 100 - libor_rate * 100