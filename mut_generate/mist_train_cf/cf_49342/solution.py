"""
QUESTION:
Create a function `count_customers_with_multiple_purchases` that takes a list of customer purchases, where each purchase is a tuple containing the customer ID and category, and returns the number of customers who made purchases in at least two different categories. The function should not use any calculated fields with other calculated fields, as this is not supported by the target platform (Quicksight).
"""

def count_customers_with_multiple_purchases(purchases):
    """
    This function takes a list of customer purchases, where each purchase is a tuple containing the customer ID and category,
    and returns the number of customers who made purchases in at least two different categories.

    Args:
        purchases (list): A list of tuples, where each tuple contains a customer ID and a category.

    Returns:
        int: The number of customers who made purchases in at least two different categories.
    """
    customer_categories = {}
    
    for customer, category in purchases:
        if customer not in customer_categories:
            customer_categories[customer] = set()
        customer_categories[customer].add(category)
    
    return sum(1 for categories in customer_categories.values() if len(categories) > 1)