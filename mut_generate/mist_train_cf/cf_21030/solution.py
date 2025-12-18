"""
QUESTION:
Create a function `get_customer_payments` that takes a customer ID and returns the total payments from the customer in the last 10 months, including the details of each payment (payment date, amount, and payment method) and the total number of payments. The function should also include the average payment amount for the customer in the last 10 months. The function should be able to query a database table named `payments` with columns `customer_id`, `payment_date`, `amount`, and `payment_method`.
"""

import pandas as pd
from datetime import datetime, timedelta

def get_customer_payments(customer_id, payments_df):
    """
    Returns the total payments from a customer in the last 10 months, 
    including the details of each payment and the total number of payments, 
    as well as the average payment amount.

    Parameters:
    customer_id (str): The ID of the customer.
    payments_df (pd.DataFrame): A DataFrame representing the payments table.

    Returns:
    tuple: A tuple containing a DataFrame of payment details, 
           the total number of payments, and the average payment amount.
    """

    # Filter payments by customer ID and date
    recent_payments = payments_df[
        (payments_df['customer_id'] == customer_id) & 
        (pd.to_datetime(payments_df['payment_date']) >= datetime.now() - timedelta(days=300))  # approximately 10 months
    ]

    # Calculate total payments
    total_payments = recent_payments.shape[0]

    # Calculate average payment amount
    average_payment = recent_payments['amount'].mean()

    return recent_payments, total_payments, average_payment