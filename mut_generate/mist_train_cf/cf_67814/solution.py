"""
QUESTION:
Given the function name `harmonious_allocation`, write a function that calculates the proportion of investment to be allocated to each of three distinct digital currencies to achieve a harmonious allocation. The currencies have the following values per unit: Bitcoin ($50,000), Ethereum ($2,000), and Litecoin ($200). The total investment sum is $100,000. The function should return the amount to be invested in each currency for a harmonious allocation, where the value in each cryptocurrency is equal.
"""

def harmonious_allocation(total_investment, bitcoin_value, ethereum_value, litecoin_value):
    """
    Calculate the harmonious allocation of investment to three digital currencies.

    Args:
        total_investment (float): The total investment sum.
        bitcoin_value (float): The value per unit of Bitcoin.
        ethereum_value (float): The value per unit of Ethereum.
        litecoin_value (float): The value per unit of Litecoin.

    Returns:
        tuple: A tuple containing the amount to be invested in each currency for a harmonious allocation.
    """

    # Calculate the value per unit of each cryptocurrency
    total_value = bitcoin_value + ethereum_value + litecoin_value

    # Calculate the investment on each cryptocurrency
    bitcoin_investment = (bitcoin_value / total_value) * total_investment
    ethereum_investment = (ethereum_value / total_value) * total_investment
    litecoin_investment = (litecoin_value / total_value) * total_investment

    return bitcoin_investment, ethereum_investment, litecoin_investment


# Example usage:
bitcoin_investment, ethereum_investment, litecoin_investment = harmonious_allocation(100000, 50000, 2000, 200)
print(f'Bitcoin investment: {bitcoin_investment}')
print(f'Ethereum investment: {ethereum_investment}')
print(f'Litecoin investment: {litecoin_investment}')