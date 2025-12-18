"""
QUESTION:
Write a function named "check_odd_even" that takes an integer "number" as input. The function should return "even" if the number is even and divisible by 4, "odd" if the number is odd and divisible by 3, and "neither" for any other integer cases. If the input is not an integer, the function should return "invalid input".
"""

def check_odd_even(number):
    if not isinstance(number, int):
        return "invalid input"
    elif number % 4 == 0:
        return "even"
    elif number % 3 == 0 and number % 2 != 0:
        return "odd"
    else:
        return "neither"