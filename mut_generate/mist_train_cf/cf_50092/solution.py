"""
QUESTION:
Create a function `avg_amount(customer_id)` that takes a customer ID as input and returns a dictionary with the customer's ID and their average transaction value. Assume the transactions data is a dictionary where the keys are customer IDs and the values are lists of transaction amounts. If the customer ID is not found, return a dictionary with an "error" message and a 404 status code.
"""

def avg_amount(customer_id, transactions_data):
    if customer_id in transactions_data:
        avg_value = sum(transactions_data[customer_id]) / len(transactions_data[customer_id])
        return {"customer_id": customer_id, "average transaction value": avg_value}
    else:
        return {"error": "Customer not found"}