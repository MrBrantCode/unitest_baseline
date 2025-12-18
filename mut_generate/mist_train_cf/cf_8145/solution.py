"""
QUESTION:
Write a program with a function named `calculate_discounted_price` to calculate the discounted price of a product, a function named `validate_float_input` to get a valid float input from the user, a function named `validate_percentage_input` to get a valid percentage input from the user, a function named `validate_string_input` to get a valid string input from the user, and a function named `print_product_info` to print the product information. 

In the `main` function, repeatedly prompt the user to enter the product name, original price, discount rate, and currency symbol until the user enters "exit" or "quit". For each product, calculate and print the discounted price, and keep track of the total discounted price of all products. After the loop, print the total discounted price.
"""

def calculate_discounted_price(original_price, discount_rate):
    return original_price * (1 - discount_rate / 100)