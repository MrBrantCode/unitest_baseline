"""
QUESTION:
Create a function called `add_values_and_seven` that takes two parameters, adds 7 to their sum, and returns the result. The function should follow PEP-8 guidelines and include a docstring describing the function's purpose, parameters, and return value. Implement exception handling to handle invalid inputs. Additionally, write a unit test function to verify the accuracy of `add_values_and_seven` with various input scenarios, including integer, float, and string inputs.
"""

def add_values_and_seven(a, b):
    """
    Returns the sum of two values and 7.

    Parameters:
    a (int or float): The first number
    b (int or float): The second number

    Returns:
    int or float: The sum of a, b and 7
    """

    try:    
        return a + b + 7
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None