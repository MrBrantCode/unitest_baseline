"""
QUESTION:
Write a function `filter_customers` that takes a list of customer names as input and returns a list of names that contain the string "ali" (case-insensitive) and do not contain any special characters or numbers. The function should consider the entire string for validation.
"""

import re

def filter_customers(customers):
    pattern = r'^[a-zA-Z\s]*ali[a-zA-Z\s]*$'
    return [customer for customer in customers if re.match(pattern, customer, re.IGNORECASE)]