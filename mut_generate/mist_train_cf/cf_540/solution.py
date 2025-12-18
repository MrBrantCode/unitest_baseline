"""
QUESTION:
Write a function `get_top_customers` that takes in a list of purchases, where each purchase is a dictionary containing customer information, product details, and purchase amount. The function should return a list of customers who have bought "Apple iPod" with a storage capacity of at least 128GB from the "Electronics" category. For each customer, calculate their total purchase amount by summing the prices of all their purchases in the "Electronics" category. Additionally, calculate the average price of all the "Apple iPod" purchases made by each customer. Sort the list of customers in descending order of their total purchase amount and within each group, sort them in descending order of their average price for "Apple iPod" purchases.

The input list of purchases is assumed to be in the following format: `purchases = [{'customer': 'John', 'product': 'Apple iPod', 'storage': 128, 'category': 'Electronics', 'price': 200}, ...]`.
"""

def get_top_customers(purchases):
    """
    Returns a list of customers who have bought "Apple iPod" with a storage capacity of at least 128GB from the "Electronics" category.
    For each customer, calculates their total purchase amount by summing the prices of all their purchases in the "Electronics" category.
    Calculates the average price of all the "Apple iPod" purchases made by each customer.
    Sorts the list of customers in descending order of their total purchase amount and within each group, 
    sorts them in descending order of their average price for "Apple iPod" purchases.

    Args:
        purchases (list): A list of purchases, where each purchase is a dictionary containing customer information, product details, and purchase amount.

    Returns:
        list: A list of customers who meet the specified criteria.
    """

    # Filter the purchases by "Apple iPod" with a storage capacity of at least 128GB from the "Electronics" category
    ipod_purchases = [purchase for purchase in purchases 
                      if purchase['product'] == 'Apple iPod' and purchase['storage'] >= 128 and purchase['category'] == 'Electronics']

    # Create a dictionary to store the total purchase amount and average price for each customer
    customer_purchases = {}
    for purchase in purchases:
        customer = purchase['customer']
        if customer not in customer_purchases:
            customer_purchases[customer] = {'total_amount': 0, 'ipod_amount': 0, 'ipod_count': 0}
        
        if purchase['category'] == 'Electronics':
            customer_purchases[customer]['total_amount'] += purchase['price']
        
        if purchase in ipod_purchases:
            customer_purchases[customer]['ipod_amount'] += purchase['price']
            customer_purchases[customer]['ipod_count'] += 1

    # Calculate the average price for each customer
    for customer, purchase_info in customer_purchases.items():
        if purchase_info['ipod_count'] > 0:
            purchase_info['average_ipod_price'] = purchase_info['ipod_amount'] / purchase_info['ipod_count']
        else:
            purchase_info['average_ipod_price'] = 0

    # Create a list of customers who have bought "Apple iPod" with a storage capacity of at least 128GB from the "Electronics" category
    top_customers = [customer for customer, purchase_info in customer_purchases.items() if purchase_info['ipod_count'] > 0]

    # Sort the list of customers in descending order of their total purchase amount and average price for "Apple iPod" purchases
    sorted_customers = sorted(top_customers, key=lambda customer: (-customer_purchases[customer]['total_amount'], -customer_purchases[customer]['average_ipod_price']))

    return sorted_customers