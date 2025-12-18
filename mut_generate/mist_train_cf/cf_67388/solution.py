"""
QUESTION:
Design a function `assign_number` that takes a series of values as input and assigns the valid numbers to a variable. The function should validate if the input values are integers ranging from 1 to 10. If a non-integer or an integer outside the range is encountered, the function should return an error message. If all input values are valid, the function should return the list of assigned numbers.

The function should handle exceptions/errors for wrong types of values passed as arguments. It should also be able to assign a single integer (5) to the variable and a list of numbers to the same variable.
"""

def assign_number(numbers):
    my_number = []
    for number in numbers:
        if isinstance(number, int) and 1<=number<=10:
            my_number.append(number)
        else:
            return "Error: Only Integers from 1 to 10 Allowed!"
    return my_number