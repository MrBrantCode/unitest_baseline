"""
QUESTION:
Write a function `greet` that takes a string input representing a number, which may be a floating-point number. The function should return a string as follows:

- If the input is not a valid number, return "Invalid number".
- If the input number is not in the range [0, 1e7], return "Number out of range".
- If the input number is divisible by both 5 and 7, return "Beautiful Day and Night".
- If the input number is divisible by 5, return "Good Day".
- If the input number is divisible by 7, return "Good Night".
- Otherwise, return "Good Evening".
"""

def greet(number):
    try:
        number = float(number)
        if number < 0 or number > 1e7:
            return "Number out of range"
        if number % 5 == 0 and number % 7 == 0:
            return "Beautiful Day and Night"
        elif number % 5 == 0:
            return "Good Day"
        elif number % 7 == 0:
            return "Good Night"
        else:
            return "Good Evening"
    except ValueError:
        return "Invalid number"