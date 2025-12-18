"""
QUESTION:
Write a query to retrieve customer names from the Orders table. The query should meet the following criteria: 
- The customer is from a specific country, 'specific_country'.
- The order was placed within a certain time frame, between 'start_date' and 'end_date'.
"""

def retrieve_customer_names(country, start_date, end_date, orders):
    """
    Retrieves customer names from a list of orders based on the country and date range.

    Args:
    country (str): The specific country to filter by.
    start_date (str): The start date of the time frame.
    end_date (str): The end date of the time frame.
    orders (list): A list of dictionaries containing order information.

    Returns:
    list: A list of customer names that match the specified criteria.
    """
    return [order['customer_name'] for order in orders 
            if order['country'] == country 
            and start_date <= order['order_date'] <= end_date]