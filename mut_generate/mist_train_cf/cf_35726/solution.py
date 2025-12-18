"""
QUESTION:
Create a function called `print_digits` that takes a four-digit positive integer as input. The function should print the individual digits in the thousands, hundreds, tens, and units places. If the input is not a four-digit positive integer, the function should print "Invalid input" and return without further processing.
"""

def print_digits(number):
    if not isinstance(number, int) or number < 1000 or number > 9999:
        print("Invalid input")
        return

    units = number % 10
    dozens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000 % 10

    print('Units:', units)
    print('Tens:', dozens)
    print('Hundreds:', hundreds)
    print('Thousands:', thousands)