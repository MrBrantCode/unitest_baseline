"""
QUESTION:
Write a function named "check_odd_even" that takes an integer "number" as input and returns "even" if the number is even, divisible by 4, a multiple of 6, and greater than 10, "odd" if the number is odd, divisible by 3, a multiple of 9, and less than 100, and "neither" for any other cases. The function should also handle the case when the input is not an integer or a string representation of an integer, and return "invalid input".
"""

def check_odd_even(number):
    if isinstance(number, int) or (isinstance(number, str) and number.isdigit()):
        number = int(number)
        if number % 2 == 0 and number % 4 == 0 and number % 6 == 0 and number > 10:
            return "even"
        elif number % 2 != 0 and number % 3 == 0 and number % 9 == 0 and number < 100:
            return "odd"
        else:
            return "neither"
    else:
        return "invalid input"