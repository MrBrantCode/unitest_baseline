"""
QUESTION:
Create a function `multiply(number1, number2)` that takes two integers as input and returns their product without using the multiplication operator. The function should work with both positive and negative integers.
"""

def multiply(number1, number2):
    result = 0

    # Handling negative numbers
    positive = False
    if (number1 < 0 and number2 < 0) or (number1 > 0 and number2 > 0):
        positive = True

    number1 = abs(number1)
    number2 = abs(number2)

    for i in range(number2):
        result += number1

    if positive:
        return result
    else:
        return -result