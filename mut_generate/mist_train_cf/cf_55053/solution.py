"""
QUESTION:
Write a Python function `ternary_operator_usage` that demonstrates the usage of ternary operators. The function should take an integer `speed` as input and return a string indicating whether the speed is normal or overspeeding based on a threshold of 100.
"""

def ternary_operator_usage(speed):
    """
    Demonstrates the usage of ternary operators to determine whether a given speed is normal or overspeeding.
    
    Args:
        speed (int): The speed value to check.
    
    Returns:
        str: A string indicating whether the speed is normal or overspeeding.
    """
    return 'You are overspeeding' if speed > 100 else 'Your speed is normal'