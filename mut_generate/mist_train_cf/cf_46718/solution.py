"""
QUESTION:
Write a function `max_of_three` that takes three parameters and returns the largest numerical value among them. The function should accept parameters of any numerical type (integers, floats, etc.) and handle potential erroneous inputs like special characters and strings by returning an error message. If any of the inputs are not numerical values, the function should return an error message.
"""

def max_of_three(num1, num2, num3):
    try:
        num1, num2, num3 = float(num1), float(num2), float(num3)  # convert inputs to float
    except ValueError:  # handle potential ValueError from inappropriate data types
        return "Invalid input. It should be numbers"
    
    return max(num1, num2, num3)  # return the maximum value