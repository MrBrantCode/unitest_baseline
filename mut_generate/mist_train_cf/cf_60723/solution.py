"""
QUESTION:
Write a function named `unfilled_or_incorrect_customer_data` that takes a list of customer data (`customer_table`) as input, where each customer is a dictionary containing 'contact_info' and 'purchase_history'. The function should return a list of customers with either missing or incorrect data. The function should consider a customer's data as missing if their 'contact_info' or 'purchase_history' is empty, and incorrect if their email address is invalid or their purchase amount is unrealistic (less than -1000 or more than 100000). The function should validate email addresses using a regular expression and handle the 'email' and 'amount' keys within the 'contact_info' and 'purchase_history' dictionaries, respectively.
"""

import re

def is_email_valid(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(email_regex, email) is not None

def is_amount_realistic(amount):
    return -1000 <= amount <= 100000 

def unfilled_or_incorrect_customer_data(customer_table):
    result = []
    for customer in customer_table:
        if not customer['contact_info'] or not customer['purchase_history']:
            result.append(customer)
        elif 'email' in customer['contact_info'] and 'amount' in customer['purchase_history']:
            if not is_email_valid(customer['contact_info']['email']) or not is_amount_realistic(customer['purchase_history']['amount']):
                result.append(customer)
    return result