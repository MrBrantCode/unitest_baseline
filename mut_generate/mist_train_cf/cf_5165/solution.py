"""
QUESTION:
Design a function named `retrieve_customer_info` that takes a customer's phone number as input and returns their name, address, and a list of their previous purchases. The function should be able to efficiently search for the customer information based on their phone number. Assume that the customer information is stored in a data structure that you choose. The function should return `None` for all values if the customer is not found.
"""

def retrieve_customer_info(phone_number, customers):
    customer_info = customers.get(phone_number)
    if customer_info:
        name = customer_info["name"]
        address = customer_info["address"]
        purchases = customer_info["purchases"]
        return name, address, purchases
    else:
        return None, None, None  # Customer not found