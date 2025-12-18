"""
QUESTION:
Design a function `perpetual_contract_resolution` that simulates the process of closing a perpetual contract position and its impact on the counterparties involved. The function should take two parameters: `initial_position` (either 'long' or 'short') and `action` (either 'close' or 'liquidate'). It should return a string describing the resolution process, including what happens to the initial counterparty. Assume the exchange takes over when a position is liquidated.
"""

def perpetual_contract_resolution(initial_position, action):
    """
    Simulates the process of closing a perpetual contract position and its impact on the counterparties involved.

    Args:
        initial_position (str): The initial position of the contract, either 'long' or 'short'.
        action (str): The action taken on the position, either 'close' or 'liquidate'.

    Returns:
        str: A string describing the resolution process, including what happens to the initial counterparty.
    """

    if action == 'close':
        # When you close a position, you are closing it with another counterparty that takes the opposite side at that time.
        # Your initial counterparty doesn't necessarily have anything to do with your decision to close the position.
        return f"When you close your {initial_position} position, you're essentially executing the opposite trade with another counterparty. " \
               f"Your initial counterparty who took the {'short' if initial_position == 'long' else 'long'} position when you went {initial_position} " \
               f"doesn't necessarily have anything to do with your decision to close the position."
    elif action == 'liquidate':
        # When you get liquidated, the exchange takes over and automatically executes the opposite trade to close the position.
        # This doesn’t really have an impact on your initial counterparty.
        return f"When you get liquidated, the exchange takes over and automatically executes the opposite trade to close your {initial_position} position. " \
               f"This doesn’t really have an impact on your initial counterparty who took the {'short' if initial_position == 'long' else 'long'} position when you went {initial_position}."
    else:
        return "Invalid action. Please choose either 'close' or 'liquidate'."