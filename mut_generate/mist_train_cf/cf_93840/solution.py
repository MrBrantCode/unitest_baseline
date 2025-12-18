"""
QUESTION:
Create a function `is_number_valid(number)` that determines whether a given number is even or odd, handling negative numbers, decimal numbers, and large numbers within the range of -10^9 to 10^9. The function should return a message indicating whether the input number is even, odd, a decimal, or outside the valid range, and handle non-numerical inputs by returning an error message.
"""

def is_number_valid(number):
    try:
        number = float(number)
        if number < -10**9 or number > 10**9:
            return "Number is outside the valid range of -10^9 to 10^9."
        elif number % 1 != 0:
            return "Number is a decimal."
        elif number % 2 == 0:
            return "Number is even."
        else:
            return "Number is odd."
    except ValueError:
        return "Input is not a valid number."