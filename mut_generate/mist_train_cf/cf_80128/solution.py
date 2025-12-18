"""
QUESTION:
Write a function `handleTransactions` that takes a list of integers `transactionOperations` and an integer `transactionsToUndo`. Implement the function to process the transactions in `transactionOperations` in order, and if the balance becomes negative, undo the last `transactionsToUndo` number of transactions. If the balance remains non-negative after undoing transactions, return the updated balance; otherwise, return 0. The function should assume that positive numbers in `transactionOperations` increase the balance and negative numbers decrease it.
"""

from typing import List

def handleTransactions(transactionOperations: List[int], transactionsToUndo: int) -> int:
    """
    Process the transactions in transactionOperations in order, and if the balance becomes negative, 
    undo the last transactionsToUndo number of transactions. If the balance remains non-negative 
    after undoing transactions, return the updated balance; otherwise, return 0.

    Args:
        transactionOperations (List[int]): A list of integers representing the transactions.
        transactionsToUndo (int): The number of transactions to undo when the balance becomes negative.

    Returns:
        int: The updated balance or 0 if it remains negative after undoing transactions.
    """
    totalBalance = 0
    previousTransactions = []

    for operation in transactionOperations:
        totalBalance += operation
        previousTransactions.append(operation)
        if totalBalance < 0:
            for _ in range(min(transactionsToUndo, len(previousTransactions))):
                undo_transaction = previousTransactions.pop()
                totalBalance -= undo_transaction
                transactionsToUndo -= 1
                if totalBalance >= 0:
                    return totalBalance
    return totalBalance if totalBalance >= 0 else 0