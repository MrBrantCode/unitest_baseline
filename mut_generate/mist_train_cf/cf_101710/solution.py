"""
QUESTION:
Write a function named `generate_summary` that takes a list of dictionaries as input, where each dictionary contains the keys "date", "product", "location", and "amount". The function should return a summary sentence that includes the unique products and locations, and the total sales amount. The summary sentence should be in the format: "Company sales for the past year include {products} sold in {locations} for a total of ${total_sales}."
"""

def generate_summary(data):
    """
    Generate a summary sentence for company sales.

    Args:
    data (list): A list of dictionaries containing sales data.
                 Each dictionary should have the keys "date", "product", "location", and "amount".

    Returns:
    str: A summary sentence including unique products, locations, and total sales amount.
    """
    # Extract the unique products and locations
    products = set([d["product"] for d in data])
    locations = set([d["location"] for d in data])
    # Calculate the total sales amount
    total_sales = sum([d["amount"] for d in data])
    # Generate the summary sentence
    return f"Company sales for the past year include {', '.join(products)} sold in {', '.join(locations)} for a total of ${total_sales}."