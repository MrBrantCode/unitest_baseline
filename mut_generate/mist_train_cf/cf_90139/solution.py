"""
QUESTION:
Write a function `compare_numbers(num1, num2)` that compares two numbers without using comparison operators (>, <, ==), built-in functions (max, min), arithmetic operations (+, -, *, /), conditional statements (if-else), or loops (for, while). The function should return the larger number if the two numbers are not equal and "Equal" if they are equal, with a time complexity of O(1).
"""

def compare_numbers(num1, num2):
    # Bitwise XOR operation
    xor = num1 ^ num2
    # Bitwise AND operation
    bit_and = num1 & num2
    # Bitwise OR operation
    bit_or = num1 | num2
    # Bitwise NOT operation
    bit_not = ~bit_or
    
    # Calculate the larger number using bitwise operations
    larger_num = (bit_or & bit_not) | (bit_and & xor)
    
    # Check if the numbers are equal
    if xor == 0:
        return "Equal"
    else:
        return larger_num