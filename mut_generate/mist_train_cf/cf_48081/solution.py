"""
QUESTION:
Determine the amounts borrowed from each of three loan types with annual interest rates of 5%, 7%, and 10%, given that the total borrowed amount is $1500, the maximum amount that can be borrowed from any single loan is $700, and the total interest paid after one year is $105.
"""

def entrance(total_borrowed, max_single_loan, total_interest, interest_rates):
    """
    Determine the amounts borrowed from each of three loan types with annual interest rates.

    Args:
    - total_borrowed (float): The total borrowed amount.
    - max_single_loan (float): The maximum amount that can be borrowed from any single loan.
    - total_interest (float): The total interest paid after one year.
    - interest_rates (list): A list of annual interest rates.

    Returns:
    - A list of amounts borrowed from each loan type.
    """
    amount_borrowed = [0] * len(interest_rates)
    amount_borrowed[0] = max_single_loan
    remaining_amount = total_borrowed - max_single_loan
    amount_borrowed[1] = min(max_single_loan, remaining_amount)
    amount_borrowed[2] = total_borrowed - amount_borrowed[0] - amount_borrowed[1]
    return amount_borrowed