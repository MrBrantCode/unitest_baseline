"""
QUESTION:
Write a function named `generate_summary` that takes a list of dictionaries as input, where each dictionary contains information about a sale, including the date, product, location, and amount. The function should return a summary sentence that includes the unique products and locations, and the total sales amount. The summary sentence should be in the format: "Company sales for the past year include {products} sold in {locations} for a total of ${total_sales}." The function should exclude the date information from the input data.
"""

def generate_summary(sales_data):
    """
    Generate a summary sentence for company sales.

    Args:
    sales_data (list): A list of dictionaries containing information about sales.

    Returns:
    str: A summary sentence that includes unique products, locations, and total sales amount.
    """
    # Extract the unique products and locations
    products = set([d["product"] for d in sales_data])
    locations = set([d["location"] for d in sales_data])

    # Calculate the total sales amount
    total_sales = sum([d["amount"] for d in sales_data])

    # Generate the summary sentence
    summary = f"Company sales for the past year include {', '.join(sorted(products))} sold in {', '.join(sorted(locations))} for a total of ${total_sales}."
    
    return summary