"""
QUESTION:
Write a function `check_independence` that determines if two events are independent based on their probabilities and calculates their correlation. The function should take as input the total number of customers who bought both products, the total number of customers who bought each product separately, and the total number of customers. It should return whether the events are independent and their correlation.
"""

def check_independence(customers_both, customers_product_a, customers_product_b, total_customers):
    """
    Determines if two events are independent based on their probabilities and calculates their correlation.

    Args:
        customers_both (int): The total number of customers who bought both products.
        customers_product_a (int): The total number of customers who bought product A.
        customers_product_b (int): The total number of customers who bought product B.
        total_customers (int): The total number of customers.

    Returns:
        tuple: A tuple containing a boolean indicating whether the events are independent and their correlation.
    """
    probability_a = customers_product_a / total_customers
    probability_b = customers_product_b / total_customers
    probability_both = customers_both / total_customers

    # Check for independence
    independent = probability_a * probability_b == probability_both

    # Calculate correlation
    correlation = "positive" if probability_both > probability_a * probability_b else "negative" if probability_both < probability_a * probability_b else "neutral"

    return independent, correlation