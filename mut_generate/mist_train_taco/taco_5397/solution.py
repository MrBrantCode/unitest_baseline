"""
QUESTION:
Lot of museum allow you to be a member, for a certain amount `amount_by_year` you can have unlimitted acces to the museum. 

In this kata you should complete a function in order to know after how many visit it will be better to take an annual pass. The function take 2 arguments `annual_price` and `individual_price`.
"""

from math import ceil

def calculate_annual_pass_break_even_visits(annual_price, individual_price):
    """
    Calculate the minimum number of visits required for the annual pass to be more cost-effective.

    Parameters:
    - annual_price (float or int): The cost of the annual pass.
    - individual_price (float or int): The cost of a single visit.

    Returns:
    - int: The minimum number of visits required.
    """
    return ceil(annual_price / individual_price)