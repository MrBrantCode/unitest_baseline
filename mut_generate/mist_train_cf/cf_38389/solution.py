"""
QUESTION:
Implement a function `select_transactions` that selects a subset of transactions with the highest fee rates from a given list, ensuring that the total size of the selected transactions does not exceed a given block size limit in bytes.

Function `select_transactions` takes two parameters: `transactions`, a list of tuples containing the transaction size in MiB and the transaction fee in satoshi, and `block_size_limit`, an integer representing the maximum block size in bytes. The function returns a list of tuples representing the selected transactions.

The function should prioritize transactions with the highest fee rates, calculated as the fee divided by the transaction size in bytes.
"""

from typing import List, Tuple

def select_transactions(transactions: List[Tuple[float, int]], block_size_limit: int) -> List[Tuple[float, int]]:
    # Calculate fee rates for each transaction
    fee_rates = [(fee / (size * 1024 * 1024), size, fee) for size, fee in transactions]
    
    # Sort transactions based on fee rates in descending order
    sorted_transactions = sorted(fee_rates, key=lambda x: x[0], reverse=True)
    
    selected_transactions = []
    total_size = 0
    for _, size, fee in sorted_transactions:
        if total_size + size <= block_size_limit:
            selected_transactions.append((size, fee))
            total_size += size
        else:
            break
    
    return selected_transactions