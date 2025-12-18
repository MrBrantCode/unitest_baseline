"""
QUESTION:
Implement a function named `add_decimal_numbers` that takes two decimal numbers as strings, adds them together using a stack data structure, and returns the result as a string. The function should handle decimal numbers of varying lengths and any potential carry values that occur during the addition.
"""

def add_decimal_numbers(num1, num2):
    """
    Adds two decimal numbers using a stack data structure.

    Args:
        num1 (str): The first decimal number.
        num2 (str): The second decimal number.

    Returns:
        str: The sum of the two decimal numbers.
    """
    stack1 = []
    stack2 = []

    # Push the digits of num1 onto stack1
    for digit in num1:
        stack1.append(digit)

    # Push the digits of num2 onto stack2
    for digit in num2:
        stack2.append(digit)

    carry = 0
    result = ""

    # Add the digits from both stacks and handle carry
    while stack1 and stack2:
        digit1 = int(stack1.pop())
        digit2 = int(stack2.pop())
        total = digit1 + digit2 + carry
        carry = total // 10
        result = str(total % 10) + result

    # Handle remaining digits in stack1
    while stack1:
        digit1 = int(stack1.pop())
        total = digit1 + carry
        carry = total // 10
        result = str(total % 10) + result

    # Handle remaining digits in stack2
    while stack2:
        digit2 = int(stack2.pop())
        total = digit2 + carry
        carry = total // 10
        result = str(total % 10) + result

    # Append remaining carry
    if carry > 0:
        result = str(carry) + result

    return result