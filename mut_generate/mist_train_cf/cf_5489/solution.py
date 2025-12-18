"""
QUESTION:
Create a function `ternary_search(start, end, secret_number)` that takes an integer range defined by `start` and `end`, and a `secret_number` within that range. Implement a ternary search algorithm to guess the `secret_number` with a time complexity of O(logN), where N is the range of possible secret numbers. The function should return the number of guesses it takes to find the `secret_number`.
"""

def ternary_search(start, end, secret_number):
    """
    Ternary search algorithm to guess the secret_number within a given range.
    
    Args:
    start (int): The start of the range.
    end (int): The end of the range.
    secret_number (int): The number to be guessed.
    
    Returns:
    int: The number of guesses it takes to find the secret_number.
    """
    guesses = 0
    
    while start <= end:
        mid1 = start + (end - start) // 3
        mid2 = end - (end - start) // 3
        
        if mid1 == secret_number:
            guesses += 1
            return guesses
        
        if mid2 == secret_number:
            guesses += 2
            return guesses
        
        guesses += 2
        
        if secret_number < mid1:
            end = mid1 - 1
        elif secret_number > mid2:
            start = mid2 + 1
        else:
            start = mid1 + 1
            end = mid2 - 1
    
    return -1