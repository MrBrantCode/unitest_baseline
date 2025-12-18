"""
QUESTION:
Create a function called `divideTwoNumbers(a, b)` that takes two arguments, 'a' and 'b'. The function should return the result of dividing 'a' by 'b' while considering the following rules: 

- If both 'a' and 'b' are integers, return the result as an integer. 
- If either 'a' or 'b' is a floating-point number, return the result as a floating-point number.
- If either 'a' or 'b' is a string, return "Invalid input! Please provide numeric values."
- If 'b' is 0, return "Division by 0 not allowed!"
"""

def divide_two_numbers(a, b):
    """
    Divide two numbers considering integer and floating-point division.
    
    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.
    
    Returns:
        int or float: The result of the division. If either 'a' or 'b' is a string, returns "Invalid input! Please provide numeric values.".
        str: "Division by 0 not allowed!" if 'b' is 0.
    """

    # Check if inputs are numeric
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input! Please provide numeric values."
    
    # Check for division by zero
    if b == 0:
        return "Division by 0 not allowed!"
    
    # Perform integer or floating-point division
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    else:
        return a / b