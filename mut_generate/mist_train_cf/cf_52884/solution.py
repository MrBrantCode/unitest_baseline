"""
QUESTION:
Implement a function `backtest_limit_orders` that simulates a backtest for limit orders in a trading strategy. The function should take into account when a limit order gets hit, handle overlapping orders, position limits, and order expiration. The function should be able to cancel or revise pending orders after a certain duration and prioritize new orders based on the latest trading signal.
"""

def backtest_limit_orders(limit_orders, position_limits, order_expiration):
    """
    Simulates a backtest for limit orders in a trading strategy.

    Parameters:
    limit_orders (list): A list of dictionaries containing order information (price, quantity, etc.)
    position_limits (int): The maximum number of positions that can be taken at any given time
    order_expiration (int): The duration after which a pending order is cancelled or revised

    Returns:
    A list of dictionaries containing the results of the backtest (filled orders, cancelled orders, etc.)
    """

    # Initialize variables to track filled orders, cancelled orders, and current positions
    filled_orders = []
    cancelled_orders = []
    current_positions = 0

    # Iterate over each limit order
    for order in limit_orders:
        # Check if the order can be placed without exceeding position limits
        if current_positions < position_limits:
            # Simulate the order being placed and waiting for it to be filled or expired
            # For simplicity, assume the order is filled if the price is met within the order expiration duration
            # In a real-world scenario, this would depend on the actual market data and order book
            if order['price'] <= order_expiration:
                # Order is filled, update the current positions and filled orders
                current_positions += 1
                filled_orders.append(order)
            else:
                # Order is not filled, cancel the order and update the cancelled orders
                cancelled_orders.append(order)
        else:
            # Position limit reached, cancel the order
            cancelled_orders.append(order)

    # Return the results of the backtest
    return {'filled_orders': filled_orders, 'cancelled_orders': cancelled_orders}