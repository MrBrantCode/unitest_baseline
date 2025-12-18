"""
QUESTION:
Create a function called hedge_basis_risk that determines the most suitable derivative instrument to hedge against basis risk due to interest rate fluctuations in an arbitrage position. The function should take in the current risk-free rate, the arbitrage position profit, and the new interest rate as inputs, and return a list of suitable derivative instruments (Interest Rate Futures, Interest Rate Swaps, Interest Rate Options).
"""

def hedge_basis_risk(risk_free_rate, arbitrage_profit, new_interest_rate):
    """
    Determine the most suitable derivative instrument to hedge against basis risk due to interest rate fluctuations in an arbitrage position.

    Args:
    risk_free_rate (float): The current risk-free rate.
    arbitrage_profit (float): The arbitrage position profit.
    new_interest_rate (float): The new interest rate.

    Returns:
    list: A list of suitable derivative instruments.
    """

    suitable_instruments = []

    # Check if interest rate has increased
    if new_interest_rate > risk_free_rate:
        # Selling interest rate futures can hedge against rising interest rates
        suitable_instruments.append("Interest Rate Futures")

        # Enter into a swap contract where you receive a fixed interest and pay a variable interest rate
        suitable_instruments.append("Interest Rate Swaps")

        # Buy a cap option that pays you when interest rates rise above a certain level
        suitable_instruments.append("Interest Rate Options")

    return suitable_instruments