"""
QUESTION:
Create a function `calculate_sales_efficiency` that takes as input two sets of sales and hours worked data for an employee over two different months, and calculates the selling efficiency of the employee. The function should also extrapolate the data for a hypothetical month where the employee works a specified number of hours, based on their past performance and trend.
"""

def calculate_sales_efficiency(sales_month1, hours_month1, sales_month2, hours_month2, future_hours):
    """
    Calculate the selling efficiency of an employee based on past performance and extrapolate data for a hypothetical month.

    Args:
    sales_month1 (float): Sales for the first month.
    hours_month1 (float): Hours worked in the first month.
    sales_month2 (float): Sales for the second month.
    hours_month2 (float): Hours worked in the second month.
    future_hours (float): Hours worked in the hypothetical month.

    Returns:
    float: The selling efficiency of the employee in the hypothetical month.
    """

    # Calculate sales per hour for each month
    sales_per_hour_month1 = sales_month1 / hours_month1
    sales_per_hour_month2 = sales_month2 / hours_month2

    # Calculate the average sales per hour
    average_sales_per_hour = (sales_per_hour_month1 + sales_per_hour_month2) / 2

    # Extrapolate data for the hypothetical month
    future_sales = average_sales_per_hour * future_hours

    return future_sales