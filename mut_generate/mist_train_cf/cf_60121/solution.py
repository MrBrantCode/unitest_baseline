"""
QUESTION:
Write a function named `check_balance` that takes two parameters: a list of transactions and a boolean flag `case_insensitive`. Each transaction is a tuple containing a string describing the transaction type and an integer for the transaction amount. The function should prioritize the transactions based on their type and amount, and update the balance accordingly. It should return `True` if the balance goes below zero at any point during the transactions, and `False` otherwise. If `case_insensitive` is `True`, the function should treat "deposit" and "Deposit" as the same transaction type.
"""

def check_balance(transactions, case_insensitive):
    """
    Checks if the balance goes below zero during a series of transactions.

    Args:
    transactions (list): A list of transactions. Each transaction is a tuple containing a string describing the transaction type and an integer for the transaction amount.
    case_insensitive (bool): A boolean flag indicating whether to treat 'deposit' and 'Deposit' as the same transaction type.

    Returns:
    bool: True if the balance goes below zero at any point during the transactions, False otherwise.
    """
    if case_insensitive:
        transactions = [(t[0].capitalize(), t[1]) for t in transactions]

    # Separate deposits and withdrawals, sort them based on the problem statement's rules
    deposits = sorted([t for t in transactions if t[0] == "Deposit"], key=lambda x: x[1], reverse=True)
    withdrawals = sorted([t for t in transactions if t[0] == "Withdrawal"], key=lambda x: x[1])

    balance = 0
    for transaction in deposits + withdrawals:
        if transaction[0] == "Deposit":
            balance += transaction[1]
        else:
            if balance < transaction[1]:
                return True
            balance -= transaction[1]
    return False