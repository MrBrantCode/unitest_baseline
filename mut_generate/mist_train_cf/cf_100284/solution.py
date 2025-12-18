"""
QUESTION:
Given a table of monthly sales data for different products, write a function `calculate_sales_difference` that takes the sales data as input and returns the difference between the highest and lowest average monthly sales. The sales data is a dictionary where the keys are product names and the values are lists of monthly sales.
"""

def calculate_sales_difference(sales_data):
    # Calculate average sales for each product
    average_sales = {product: sum(sales) / len(sales) for product, sales in sales_data.items()}
    
    # Find the highest and lowest average sales
    highest_average = max(average_sales.values())
    lowest_average = min(average_sales.values())
    
    # Return the difference between the highest and lowest average sales
    return highest_average - lowest_average