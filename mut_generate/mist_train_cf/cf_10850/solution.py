"""
QUESTION:
Create a function `divide_numbers` that takes a list of integers and a divisor as input. The function should divide each number in the list by the divisor, handling both positive and negative numbers. Return the result as a list of integers, performing division using basic arithmetic operations.
"""

def divide_numbers(numbers, divisor):
    result = []
    for number in numbers:
        if number < 0:
            result.append(-((-number) // divisor))
        else:
            result.append(number // divisor)
    return result