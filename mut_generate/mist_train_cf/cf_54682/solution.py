"""
QUESTION:
Given a set of purchase records, write a function `find_frequently_bought_together` to identify products that are often bought together. The function should take as input a list of transactions, where each transaction is a list of product IDs, and return a list of tuples, where each tuple contains two products that are frequently bought together. The function should use an algorithm that can efficiently handle large transaction data. The number of transactions and products is not limited.
"""

from collections import defaultdict
from itertools import combinations

def find_frequently_bought_together(transactions, min_support):
    """
    Find products that are often bought together.

    Args:
        transactions (list): A list of transactions, where each transaction is a list of product IDs.
        min_support (int): The minimum number of transactions where two products are bought together to be considered frequent.

    Returns:
        list: A list of tuples, where each tuple contains two products that are frequently bought together.
    """
    # Create a dictionary to store the frequency of each product pair
    product_pairs = defaultdict(int)
    
    # Iterate over each transaction
    for transaction in transactions:
        # Generate all possible pairs of products in the transaction
        pairs = list(combinations(transaction, 2))
        
        # Increment the frequency of each pair
        for pair in pairs:
            product_pairs[pair] += 1
    
    # Filter pairs with frequency greater than or equal to min_support
    frequent_pairs = [pair for pair, freq in product_pairs.items() if freq >= min_support]
    
    return frequent_pairs