"""
QUESTION:
Create a function called ois_swap_rate_behavior that explains the behavior of OIS swap rates when we receive or pay OIS swap rates. The function should take a string parameter describing the action, either 'receive' or 'pay', and return a string describing the effect on the swap rates. The function should not take any other parameters.
"""

def ois_swap_rate_behavior(action):
    """
    This function explains the behavior of OIS swap rates when we receive or pay OIS swap rates.

    Args:
        action (str): A string describing the action, either 'receive' or 'pay'.

    Returns:
        str: A string describing the effect on the swap rates.
    """
    if action.lower() == 'receive':
        return "When we receive OIS swap rates, the swap rates tend to fall due to increased demand."
    elif action.lower() == 'pay':
        return "When we pay OIS swap rates, the swap rates tend to rise due to increased supply."
    else:
        return "Invalid action. Please enter either 'receive' or 'pay'."