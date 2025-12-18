"""
QUESTION:
Create a function called `discount_power_derivative` that determines whether a power derivative should be discounted and which curve should be used for that purpose. The function should consider that power cannot be stored for future delivery, and thus traditional risk-free rates may not accurately reflect the risks involved. The function should also consider geographical and regulatory constraints that affect power market pricing. The output should be a discount rate that takes into account credit risk associated with counterparties in these transactions.
"""

def discount_power_derivative(irs_rate, credit_spread):
    """
    Calculate the discount rate for power derivatives.

    Args:
        irs_rate (float): Interest rate swap rate.
        credit_spread (float): Credit spread to account for credit risk.

    Returns:
        float: Discount rate for power derivatives.
    """
    # Calculate the discount rate by adjusting the irs_rate with credit_spread
    discount_rate = irs_rate + credit_spread
    return discount_rate