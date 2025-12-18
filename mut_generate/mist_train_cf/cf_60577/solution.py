"""
QUESTION:
Design a function named `handle_data` that takes a deeply nested JSON object, a product type, an attribute, an operation, and a value as input. The function should modify the specified attribute of the given product type in the JSON object based on the provided operation and value. The function should handle potential KeyError exceptions that may occur if an attribute or product type does not exist in the JSON structure, and it should also handle unsupported operations. The function should return the modified JSON object or an error message if an exception occurs. The operation can be either 'increment' or 'decrement'.
"""

import json

# Function to handle data manipulation based on conditions
def handle_data(json_obj, product_type, attr, operation, value):
    try:
        product_list = json_obj["products"][product_type]
    except KeyError:
        return "Product type not found"

    for product in product_list:
        try:
            if operation == 'increment':
                product[attr] += value
            elif operation == 'decrement':
                product[attr] -= value
            else:
                return "Operation not supported"
        except KeyError:
            continue
    return json_obj