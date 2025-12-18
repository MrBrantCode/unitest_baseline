"""
QUESTION:
Develop a function `calculate_total` to calculate the total amount of an order. The function should take in the quantities of two products, A and B, and their corresponding prices and tax rates as parameters. The tax rates and prices have default values of 5 and 0.1 for Product A, and 10 and 0.15 for Product B, respectively. Calculate the total amount by adding the total price of each product and their corresponding taxes.
"""

def calculate_total(product_a_quantity, 
                    product_b_quantity, 
                    price_for_product_a=5, 
                    price_for_product_b=10, 
                    tax_rate_product_a=0.1, 
                    tax_rate_product_b=0.15):
    """
    Calculate the total amount of an order.

    Args:
        product_a_quantity (int): The quantity of Product A.
        product_b_quantity (int): The quantity of Product B.
        price_for_product_a (float, optional): The price of Product A. Defaults to 5.
        price_for_product_b (float, optional): The price of Product B. Defaults to 10.
        tax_rate_product_a (float, optional): The tax rate of Product A. Defaults to 0.1.
        tax_rate_product_b (float, optional): The tax rate of Product B. Defaults to 0.15.

    Returns:
        float: The total amount of the order.
    """
    total_price_product_a = product_a_quantity * price_for_product_a 
    total_tax_product_a = total_price_product_a * tax_rate_product_a 

    total_price_product_b = product_b_quantity * price_for_product_b 
    total_tax_product_b = total_price_product_b * tax_rate_product_b 

    total_order_amount = (total_price_product_a + total_tax_product_a +  
                          total_price_product_b + total_tax_product_b)

    return total_order_amount