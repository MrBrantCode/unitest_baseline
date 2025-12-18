"""
QUESTION:
Create a function named `overdraft_times` that accepts a list of integers representing banking transaction operations and an integer limit. The function should return the count of total instances where the balance dipped below the specified limit. The balance is calculated by summing the operations, and the function should return the total occurrences where the balance was below the limit.
"""

from typing import List

def overdraft_times(operations: List[int], limit: int) -> int:
    """
    Function to calculate the total instances the balance dips below a specified limit after performing a list of operations.
    :param operations: List of banking operations to perform.
    :param limit: Specified limit.
    :return: Count of instances where balance dips below specified limit.

    """
    # Initializing balance and counter
    balance = 0
    count = 0 

    # Iterating over operations
    for op in operations:
        # Calculate the new balance after performing operation
        balance += op

        # Check if balance is below limit
        if balance < limit: 
            # Increment count if balance is below limit
            count += 1 

    # Return the total occurrences where balance was below limit
    return count