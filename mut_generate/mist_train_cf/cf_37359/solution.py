"""
QUESTION:
Create a function `withdraw_cash(amount)` that takes an integer `amount` as input and returns a dictionary containing the count of each banknote denomination (50, 20, 10, 1) required to fulfill the withdrawal. The function should use the available banknotes in the most efficient way, starting from the highest denomination. It must handle non-positive and non-integer input amounts by returning a descriptive error message.
"""

def withdraw_cash(amount):
    if not isinstance(amount, int) or amount <= 0:
        return "Invalid input amount"

    banknotes = [50, 20, 10, 1]
    result = {}
    remaining_amount = amount

    for note in banknotes:
        count = remaining_amount // note
        result[note] = count
        remaining_amount -= count * note

    return result