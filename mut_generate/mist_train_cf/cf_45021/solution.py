"""
QUESTION:
Write a function named `calculate_remaining_amount` that takes two parameters: `initial_amount` and `amount_spent`, and returns the remaining amount after `amount_spent` is subtracted from `initial_amount`. The function should not take any other input and should only return the calculated remaining amount.
"""

def calculate_remaining_amount(initial_amount, amount_spent):
    """
    Calculate the remaining amount after subtracting amount_spent from initial_amount.

    Args:
        initial_amount (float): The initial amount.
        amount_spent (float): The amount spent.

    Returns:
        float: The remaining amount.
    """
    return initial_amount - amount_spent