"""
QUESTION:
Write a function `evaluate_equation(equation)` that takes a string equation as input, evaluates it using the BODMAS rule, and returns the result in both decimal and binary form. The input equation can contain basic arithmetic operations (+, -, *, /) and exponentiation (^). The function should handle any valid equation that follows the BODMAS rule.
"""

def evaluate_equation(equation):
    # Replace '^' with '**' for exponentiation
    equation = equation.replace('^', '**')
    # Evaluate the equation using eval() function
    result = eval(equation)
    # Convert the result to binary form
    if result % 1 == 0:
        binary_result = bin(int(result))[2:]
    else:
        decimal_part = result - int(result)
        decimal_binary = ''
        while decimal_part > 0:
            decimal_part *= 2
            binary_digit = int(decimal_part)
            if binary_digit == 1:
                decimal_part -= binary_digit
                decimal_binary += '1'
            else:
                decimal_binary += '0'
        binary_result = bin(int(result))[2:] + '.' + decimal_binary
    # Return the result in decimal and binary form
    return result, binary_result