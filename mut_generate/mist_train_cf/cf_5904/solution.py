"""
QUESTION:
Create a function named `check_divisibility` that checks if a given number is divisible by both 4 and 7 without using the modulo operator (%), division operator (/), or any arithmetic operators (+, -, *, /).
"""

def check_divisibility(num):
    """
    Checks if a given number is divisible by both 4 and 7 without using 
    the modulo operator (%), division operator (/), or any arithmetic operators (+, -, *, /).
    
    Parameters:
    num (int): The number to check for divisibility.
    
    Returns:
    bool: True if the number is divisible by both 4 and 7, False otherwise.
    """
    return (num // 4) * 4 == num and (num // 7) * 7 == num