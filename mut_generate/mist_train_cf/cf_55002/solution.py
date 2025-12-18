"""
QUESTION:
Create a function `calculate_increment` that takes in two arguments, `initial_weekly_gross_pay` and `new_weekly_gross_pay`, representing Peter's initial and new weekly gross pay, respectively. Calculate the difference between the new and initial weekly gross pay, and return the result. The function should handle decimal numbers and the result should be rounded to two decimal places.
"""

def calculate_increment(initial_weekly_gross_pay, new_weekly_gross_pay):
    """
    Calculate the difference between the new and initial weekly gross pay.

    Args:
        initial_weekly_gross_pay (float): Peter's initial weekly gross pay.
        new_weekly_gross_pay (float): Peter's new weekly gross pay.

    Returns:
        float: The increment in Peter's gross pay on a weekly basis due to the raise, rounded to two decimal places.
    """
    increment = new_weekly_gross_pay - initial_weekly_gross_pay
    return round(increment, 2)