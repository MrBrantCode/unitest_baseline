"""
QUESTION:
Create a function `find_digit_in_number` that takes two parameters: `number` (an integer) and `digit` (an integer). The function should return the number of occurrences of `digit` in `number`. The function must include error handling to handle cases where `number` or `digit` is not an integer, or if the input is invalid.
"""

def find_digit_in_number(number, digit):
    try:
        count = 0
        for i in str(number):
            if i == str(digit):
                count += 1
        return count
    except Exception as e:
        return f"An error occurred: {str(e)}"