"""
QUESTION:
Write a function called `exclude_numbers` that takes a list of positive integers as input and returns a comma-separated string of the numbers that are not divisible by 3 and do not contain the digit 5. If the input list is empty, the function should return an empty string.
"""

def exclude_numbers(numbers):
    output = ""
    for num in numbers:
        if num % 3 != 0 and '5' not in str(num):
            output += str(num) + ", "
    if output != "":
        output = output[:-2]  # remove the last comma and space
    return output