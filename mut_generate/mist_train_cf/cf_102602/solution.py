"""
QUESTION:
Create a function named `validate_transaction` that takes two parameters: `transaction_id` and `transaction_amount`. This function should return "Valid" if the transaction is valid and "Invalid" otherwise. A valid transaction is defined as a transaction with a positive transaction ID and a non-negative transaction amount.
"""

def validate_transaction(transaction_id, transaction_amount):
    """
    This function validates a transaction based on its ID and amount.
    
    Args:
    transaction_id (int): The ID of the transaction.
    transaction_amount (float): The amount of the transaction.
    
    Returns:
    str: "Valid" if the transaction is valid, "Invalid" otherwise.
    """
    if transaction_id > 0 and transaction_amount >= 0:
        return "Valid"
    else:
        return "Invalid"