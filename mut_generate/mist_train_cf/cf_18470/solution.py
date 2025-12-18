"""
QUESTION:
Write a function called `convert_base` that takes three parameters: a string of numbers and two integers representing the current base and the desired base. The function should convert the string from the current base to the desired base. The function should support bases 2-36 and the string should only contain valid digits for the specified base.
"""

def convert_base(string, current_base, desired_base):
    converted_number = 0
    power = 0

    for digit in string[::-1]:
        value = int(digit, current_base)
        converted_number += value * (current_base ** power)
        power += 1

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while converted_number:
        digit = converted_number % desired_base
        result = digits[digit] + result
        converted_number //= desired_base
    if not result:
        return '0'
    return result