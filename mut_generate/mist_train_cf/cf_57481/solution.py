"""
QUESTION:
Write a function `nth_odd_number(n)` and `validate_input(input_value)` to find the nth odd number and validate the user's input respectively. `nth_odd_number(n)` should return the nth odd number where n is a positive integer. `validate_input(input_value)` should return the input value if it is a positive integer, otherwise, it should print an error message and return None. The program should also generate and print odd numbers from 1 to 50, calculate their sum, average, smallest, and largest numbers. 

The function should not take any arguments other than the function parameters, and the input for the nth odd number should be taken from the user.
"""

def nth_odd_number(n):
    return (2 * n) - 1

def validate_input(input_value):
    try:
        num = int(input_value);
        if num > 0:
            return num
        else:
            print('ERROR: Please input a positive integer.')
    except ValueError:
        print('ERROR: Please input a valid integer.')