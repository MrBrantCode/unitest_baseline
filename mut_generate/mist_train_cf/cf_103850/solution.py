"""
QUESTION:
Create a function named `calculate_net_pay` that takes the number of hours worked, hourly rate, and tax rate as input, calculates the net pay by first determining the gross pay and then subtracting the tax amount, and returns the net pay. The inputs and outputs should be floating-point numbers.
"""

def calculate_net_pay(hours_worked: float, hourly_rate: float, tax_rate: float) -> float:
    """
    Calculate the net pay by determining the gross pay and subtracting the tax amount.

    Args:
        hours_worked (float): The number of hours worked.
        hourly_rate (float): The hourly rate.
        tax_rate (float): The tax rate.

    Returns:
        float: The net pay.
    """
    gross_pay = hours_worked * hourly_rate
    tax_amount = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - tax_amount
    return net_pay