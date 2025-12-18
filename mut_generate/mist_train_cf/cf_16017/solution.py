"""
QUESTION:
Write a function named "check_odd_even" that takes an integer "number" as input. The function should return "even" if the number is even, divisible by 4, and a multiple of 6, "odd" if the number is odd, divisible by 3, and a multiple of 9, and "neither" for any other cases. If the input is not an integer or a string representation of an integer, the function should return "invalid input".
"""

def check_odd_even(number):
    if isinstance(number, int) or (isinstance(number, str) and number.isdigit()):
        number = int(number)
        if number % 2 == 0:
            if number % 4 == 0 and number % 6 == 0:
                return "even"
            else:
                return "neither"
        elif number % 3 == 0 and number % 9 == 0:
            return "odd"
        else:
            return "neither"
    else:
        return "invalid input"