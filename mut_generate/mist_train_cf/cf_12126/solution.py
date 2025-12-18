"""
QUESTION:
Convert a number from a given base to a target base and return the result as a string. The function `convert_base(number, base, target_base)` takes a string `number`, an integer `base` between 2 and 36, and an integer `target_base` between 2 and 36. The function should handle numbers up to 10^18 and use the standard base conversion algorithm.
"""

def convert_base(number, base, target_base):
    # Define the digits for bases larger than 10
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Convert the number to base 10
    base_10 = 0
    power = 0
    for digit in reversed(str(number)):
        base_10 += digits.index(digit) * (base ** power)
        power += 1

    # Convert the base 10 number to the target base
    result = ""
    while base_10 > 0:
        remainder = base_10 % target_base
        result = digits[remainder] + result
        base_10 //= target_base

    return result