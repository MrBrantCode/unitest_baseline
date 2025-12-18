"""
QUESTION:
Implement a recursive function `recursive_calculation(expression)` that takes a mathematical expression as a list of numbers and operators, evaluates the expression following the order of operations, and returns the final result rounded to the nearest whole number. The function should not use built-in arithmetic operators for the final calculation but can use them for intermediate steps.
"""

def recursive_calculation(expression):
    """
    Evaluates a mathematical expression following the order of operations.
    
    Args:
    expression (list): A list of numbers and operators.
    
    Returns:
    int: The final result rounded to the nearest whole number.
    """
    
    def add(x, y):
        """Custom addition function."""
        sum = 0
        for _ in range(y):
            sum += 1
        return x + sum
    
    def subtract(x, y):
        """Custom subtraction function."""
        diff = x
        for _ in range(y):
            diff -= 1
        return diff
    
    def multiply(x, y):
        """Custom multiplication function."""
        product = 0
        for _ in range(y):
            product = add(product, x)
        return product
    
    def divide(x, y):
        """Custom division function."""
        quotient = 0
        while x >= y:
            x = subtract(x, y)
            quotient = add(quotient, 1)
        return quotient
    
    if len(expression) == 1:
        return round(expression[0])
    
    if expression[1] == '+':
        return recursive_calculation([add(expression[0], expression[2])] + expression[3:])
    elif expression[1] == '-':
        return recursive_calculation([subtract(expression[0], expression[2])] + expression[3:])
    elif expression[1] == '*':
        return recursive_calculation([multiply(expression[0], expression[2])] + expression[3:])
    elif expression[1] == '/':
        return recursive_calculation([divide(expression[0], expression[2])] + expression[3:])
    else:
        return recursive_calculation(expression[1:])