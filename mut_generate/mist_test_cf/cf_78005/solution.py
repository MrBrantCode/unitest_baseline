"""
QUESTION:
Write a function called `distribute_equally` to divide a given sum into equal parts among a specified number of people. The function should return the amount each person receives and the amount left undistributed.
"""

def distribute_equally(total_sum, people):
    """
    Divide a given sum into equal parts among a specified number of people.

    Args:
    total_sum (int): The total amount to be distributed.
    people (int): The number of people among whom the amount is to be distributed.

    Returns:
    tuple: A tuple containing the amount each person receives and the amount left undistributed.
    """
    each_gets = total_sum // people
    amount_left = total_sum % people
    return each_gets, amount_left