"""
QUESTION:
The new £5 notes have been recently released in the UK and they've certainly became a sensation! Even those of us who haven't been carrying any cash around for a while, having given in to the convenience of cards, suddenly like to have some of these in their purses and pockets. But how many of them could you get with what's left from your salary after paying all bills? The programme that you're about to write will count this for you!

Given a salary and the array of bills, calculate your disposable income for a month and return it as a number of new £5 notes you can get with that amount. If the money you've got (or do not!) doesn't allow you to get any £5 notes return 0.

£££ GOOD LUCK! £££
"""

def calculate_new_notes(salary, bills):
    """
    Calculate the number of new £5 notes that can be obtained from the disposable income after paying all bills.

    Parameters:
    salary (int or float): The total salary for the month.
    bills (list of int or float): An array of bills that need to be paid from the salary.

    Returns:
    int: The number of new £5 notes that can be obtained from the disposable income.
    """
    disposable_income = max(salary - sum(bills), 0)
    return disposable_income // 5