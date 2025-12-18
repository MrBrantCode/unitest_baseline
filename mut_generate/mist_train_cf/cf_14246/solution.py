"""
QUESTION:
Write a function `separate_and_sum_numbers` that takes a string `s` as input and returns the sum of all the numbers separated from non-numeric characters in the string. The function should not use any built-in functions or libraries that directly solve the problem.
"""

def separate_and_sum_numbers(s):
    current_number = 0
    sum_of_numbers = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            sum_of_numbers += current_number
            current_number = 0

    # Add the last number to the sum
    sum_of_numbers += current_number

    return sum_of_numbers