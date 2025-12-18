"""
QUESTION:
Implement a function named `multiply` that takes two integers `x` and `y` as input and returns their product without using any built-in arithmetic operators for multiplication. Additionally, implement another function `get_valid_input` to handle user input for a number and its limit, ensuring that the inputs are valid positive integers. Use these functions to print a multiplication table for the given number up to the specified limit.
"""

def multiply(x, y):
    """
    This function multiplies two integers x and y without using built-in arithmetic operators for multiplication.
    
    Parameters:
    x (int): The first integer to be multiplied.
    y (int): The second integer to be multiplied.
    
    Returns:
    int: The product of x and y.
    """
    result = 0
    for _ in range(y):
        result += x
    return result

def get_valid_input(prompt):
    """
    This function handles user input for a number and its limit, ensuring that the inputs are valid positive integers.
    
    Parameters:
    prompt (str): The prompt to be displayed to the user.
    
    Returns:
    int: The valid positive integer input by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: Negative numbers are not allowed. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")