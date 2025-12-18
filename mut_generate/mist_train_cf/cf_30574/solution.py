"""
QUESTION:
Write a function `calculate_payment` that takes two parameters, `purchase_amount` and `payment_method`, and returns the final amount to be paid and the installment details. The payment methods are as follows:
- Method 1: 10% discount on the purchase amount.
- Method 2: 5% discount on the purchase amount.
- Method 3: No discount or surcharge, with 2x payment installment details.
- Method 4: 20% surcharge on the purchase amount, with 3x payment installment details.
- Any other method: Error message.
The function should handle these calculations based on the chosen payment method and return the final amount and installment details.
"""

def calculate_payment(purchase_amount, payment_method):
    """
    Calculate the final amount to be paid and the installment details based on the chosen payment method.

    Args:
    purchase_amount (float): The initial purchase amount.
    payment_method (int): The chosen payment method (1, 2, 3, or 4).

    Returns:
    tuple: A tuple containing the final amount to be paid and the installment details.
    """
    if payment_method == 1:
        # 10% discount on the purchase amount
        final_amount = purchase_amount - (purchase_amount * 0.10)
        installment_details = None
    elif payment_method == 2:
        # 5% discount on the purchase amount
        final_amount = purchase_amount - (purchase_amount * 0.05)
        installment_details = None
    elif payment_method == 3:
        # No discount or surcharge, with 2x payment installment details
        final_amount = purchase_amount
        installment_details = f'2x of {final_amount/2}'
    elif payment_method == 4:
        # 20% surcharge on the purchase amount, with 3x payment installment details
        final_amount = purchase_amount + (purchase_amount * 0.20)
        installment_details = f'3x of {final_amount/3}'
    else:
        # Error message for invalid payment method
        return 'You have entered an invalid payment method.', None

    return final_amount, installment_details