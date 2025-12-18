"""
QUESTION:
Write a function called `check_divisibility` that takes a positive integer as an argument. The function should print "even" if the number is divisible by 4 and not divisible by 3, "odd" if the number is divisible by 3 and not divisible by 4, "both" if the number is divisible by both 4 and 3, and "neither" if the number is neither divisible by 4 nor by 3. The function should handle non-positive integers and non-integer inputs by printing an error message.
"""

def check_divisibility(number):
    if not isinstance(number, int) or number <= 0:
        print("Error: The input must be a positive integer")
        return

    if number % 4 == 0 and number % 3 == 0:
        print("both")
    elif number % 4 == 0:
        print("even")
    elif number % 3 == 0:
        print("odd")
    else:
        print("neither")