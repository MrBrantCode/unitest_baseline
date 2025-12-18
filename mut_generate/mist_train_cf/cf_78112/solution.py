"""
QUESTION:
Write a function `calculate_ticket_sales_difference` that takes the number of youth tickets, price per youth ticket, number of adult tickets, and price per adult ticket as inputs, and returns the difference between the total sales of adult tickets and youth tickets. The function should not take any other inputs.
"""

def calculate_ticket_sales_difference(youth_tickets, youth_price, adult_tickets, adult_price):
    """
    Calculate the difference between the total sales of adult tickets and youth tickets.

    Args:
        youth_tickets (int): Number of youth tickets sold.
        youth_price (int): Price per youth ticket.
        adult_tickets (int): Number of adult tickets sold.
        adult_price (int): Price per adult ticket.

    Returns:
        int: The difference between the total sales of adult tickets and youth tickets.
    """
    youth_sales = youth_tickets * youth_price
    adult_sales = adult_tickets * adult_price
    return adult_sales - youth_sales