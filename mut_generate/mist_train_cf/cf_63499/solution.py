"""
QUESTION:
Write a function `cross_currency_swap_risks` that determines the risks involved in different types of cross currency swaps. The function should take an integer as input, where 1 represents a float vs float swap, 2 represents a fixed vs fixed swap, and 3 represents a float vs fixed swap, and an additional input to represent whether the swap is an FX swap or not.
"""

def cross_currency_swap_risks(swap_type, is_fx_swap):
    """
    Determine the risks involved in different types of cross currency swaps.

    Args:
        swap_type (int): 1 for float vs float swap, 2 for fixed vs fixed swap, 3 for float vs fixed swap
        is_fx_swap (bool): Whether the swap is an FX swap or not

    Returns:
        list: A list of risks involved in the swap
    """

    risks = []

    if is_fx_swap:
        risks.extend(["FX risk", "interest rate risk"])
    else:
        risks.extend(["FX risk", "interest rate risk", "cross-currency basis risk"])

    if swap_type == 1:
        risks.append("floating interest rate risk")
    elif swap_type == 2:
        risks.append("limited interest rate risk")
    elif swap_type == 3:
        risks.extend(["floating interest rate risk", "fixed interest rate risk"])

    return risks