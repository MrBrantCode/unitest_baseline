"""
QUESTION:
Write a function named `calculate_pay` that takes the number of hours worked and the hourly rate as input and returns the total pay. If the number of hours worked is less than or equal to 40, the pay is the product of hours worked and hourly rate. Otherwise, the pay is calculated by paying the first 40 hours at the regular rate and any additional hours at 1.5 times the regular rate.
"""

def calculate_pay(hours_worked, hourly_rate):
    """
    Calculate the total pay based on the number of hours worked and the hourly rate.

    Args:
        hours_worked (float): The number of hours worked.
        hourly_rate (float): The hourly rate.

    Returns:
        float: The total pay.
    """
    if hours_worked <= 40:
        return hours_worked * hourly_rate
    else:
        return (40 * hourly_rate) + ((hours_worked - 40) * (hourly_rate * 1.5))