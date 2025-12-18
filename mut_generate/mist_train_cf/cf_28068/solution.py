"""
QUESTION:
Implement the `get_recommended_gas_fee` function that takes a list of tuples as input, where each tuple contains a gas price and the corresponding number of pending transactions at that price. The function should calculate the weighted average of gas prices based on the pending transactions and return the recommended gas fee. If the recommended fee exceeds the `max_gas_fee`, it should return the `max_gas_fee` instead. Assume that `max_gas_fee` is a given constant.
"""

def get_recommended_gas_fee(max_gas_fee, pending_transactions):
    """
    Calculate the weighted average of gas prices based on the pending transactions and return the recommended gas fee.

    Args:
    max_gas_fee (float): The maximum allowed gas fee.
    pending_transactions (list[tuple[float, int]]): A list of tuples, where each tuple contains a gas price and the corresponding number of pending transactions at that price.

    Returns:
    float: The recommended gas fee, capped at max_gas_fee.
    """

    # Calculate the total number of transactions
    total_transactions = sum(count for _, count in pending_transactions)

    # Calculate the weighted sum of gas prices
    weighted_prices = sum(price * count for price, count in pending_transactions)

    # Calculate the weighted average gas price
    recommended_fee = weighted_prices / total_transactions if total_transactions > 0 else 0

    # Return the recommended fee, capped at max_gas_fee
    return min(recommended_fee, max_gas_fee)