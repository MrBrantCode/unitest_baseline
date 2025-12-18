"""
QUESTION:
Implement the `replace_chain` function to replace the existing blockchain with a new one if the new chain is longer and valid. The function should perform the following steps:
1. Check if the new chain received from the network is longer than the current chain.
2. Verify the validity of the new chain using the `is_valid_chain` function.
3. If the new chain is valid and longer, replace the current chain with the new chain.
The function should return a boolean value indicating whether the chain was replaced or not. Assume the new chain is received as JSON in the request and 'blockchain' is the variable holding the current chain.
"""

def replace_chain(blockchain, new_chain, is_valid_chain):
    if new_chain is None or len(new_chain) <= len(blockchain):
        return False

    if is_valid_chain(new_chain):
        blockchain = new_chain
        return True
    else:
        return False