"""
QUESTION:
Write a function `calculate_sales_disparity` that takes a 2D list of monthly sales data as input, where each inner list represents a month and contains the sales of products A, B, and C in that month. The function should calculate the monthly sales average for each product, then return the disparity between the highest and lowest averages.
"""

def calculate_sales_disparity(sales_data):
    """
    Calculate the disparity between the highest and lowest monthly sales averages for each product.

    Args:
        sales_data (list): A 2D list of monthly sales data, where each inner list represents a month
            and contains the sales of products A, B, and C in that month.

    Returns:
        float: The disparity between the highest and lowest monthly sales averages.
    """
    # Transpose the sales data to group sales by product
    product_sales = list(map(list, zip(*sales_data)))

    # Calculate the average sales for each product
    product_averages = [sum(sales) / len(sales) for sales in product_sales]

    # Calculate the disparity between the highest and lowest averages
    disparity = max(product_averages) - min(product_averages)

    return disparity