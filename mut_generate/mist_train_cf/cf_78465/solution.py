"""
QUESTION:
Write a function named `calculate_swap_coupon_payment` to calculate the swap coupon payment for a vanilla swap trade. The function should take the following parameters: `notional`, `fixed_rate`, `floating_rate`, `years`, and `payment_frequency`. The payment frequency should be expressed as a fraction of a year. The function should return the swap coupon payment.
"""

def calculate_swap_coupon_payment(notional, fixed_rate, floating_rate, years, payment_frequency):
    """
    Calculate the swap coupon payment for a vanilla swap trade.

    Parameters:
    notional (float): The notional amount of the swap.
    fixed_rate (float): The fixed interest rate of the swap.
    floating_rate (float): The floating interest rate of the swap.
    years (int): The number of years the swap is in effect.
    payment_frequency (float): The payment frequency as a fraction of a year.

    Returns:
    float: The swap coupon payment.
    """
    # Calculate the total number of payments
    num_payments = int(years / payment_frequency)

    # Calculate the fixed coupon payment
    fixed_coupon_payment = notional * fixed_rate * payment_frequency

    # Calculate the floating coupon payment
    floating_coupon_payment = notional * floating_rate * payment_frequency

    # Return the fixed and floating coupon payments
    return fixed_coupon_payment, floating_coupon_payment