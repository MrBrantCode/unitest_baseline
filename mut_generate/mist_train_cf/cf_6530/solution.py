"""
QUESTION:
Implement a function `is_armstrong_number(num: int) -> bool` that checks if a given number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits. The function should handle negative numbers and non-integer inputs. It should also return `False` for any number that is less than -1,000,000 or greater than 1,000,000, and for any sum of digits that exceeds 1,000,000.
"""

def is_armstrong_number(num: int) -> bool:
    # Check if the input is a non-integer
    if not isinstance(num, int):
        return False

    # Check if the number is outside the range of -1,000,000 to 1,000,000
    if num < -1000000 or num > 1000000:
        return False

    # Convert the number to a string to access individual digits
    num_str = str(num)

    # Check if the number is negative
    if num < 0:
        # Exclude the negative sign from the string and convert the remaining digits back to integers
        digits = [int(digit) for digit in num_str[1:]]
    else:
        digits = [int(digit) for digit in num_str]

    # Calculate the number of digits in the number
    num_digits = len(digits)

    # Raise each digit to the power of the number of digits and sum them
    digit_sum = sum([digit ** num_digits for digit in digits])

    # Check if the sum exceeds 1,000,000
    if digit_sum > 1000000:
        return False

    # Check if the sum is equal to the original number
    if digit_sum == abs(num):
        return True

    return False