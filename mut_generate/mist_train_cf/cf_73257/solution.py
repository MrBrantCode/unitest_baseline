"""
QUESTION:
Write a SQL UPDATE statement to modify the value '5' in the 'amount' column of the 'payments' table. The update should be applied to all rows where the current value of 'amount' is '5'. You must provide a specific condition to identify the row(s) to be updated, as the provided solution will modify all rows with the specified amount.
"""

def update_amount(amount_value):
    query = f"UPDATE payments SET amount = {amount_value} WHERE amount = 5;"
    return query