"""
QUESTION:
Given a binary string `S` and a positive integer `N`, determine if for every integer `X` from 1 to `N`, the binary representation of `X` can be found as a substring within `S`. The function should return `True` if all binary representations are found and `False` otherwise. The function should be named `queryString`. The length of `S` is between 1 and 1000, and `N` is between 1 and 10^9.
"""

def queryString(S, N):
    """
    This function checks if for every integer X from 1 to N, 
    the binary representation of X can be found as a substring within S.

    Parameters:
    S (str): A binary string.
    N (int): A positive integer.

    Returns:
    bool: True if all binary representations are found, False otherwise.
    """
    
    # Iterate over each integer X from 1 to N
    for X in range(1, N + 1):
        # Convert X to binary and remove the '0b' prefix
        binary_X = bin(X)[2:]
        
        # If binary_X is not a substring of S, return False
        if binary_X not in S:
            return False
            
    # If we've checked all integers and haven't returned False, return True
    return True