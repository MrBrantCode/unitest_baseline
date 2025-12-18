"""
QUESTION:
A [Narcissistic Number](https://en.wikipedia.org/wiki/Narcissistic_number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):
```
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```
and 1634 (4 digits):
```
    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
```

The Challenge:

Your code must return **true or false** depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
"""

def is_narcissistic(number: int) -> bool:
    """
    Determines if a given number is a Narcissistic number.

    A Narcissistic number is a positive number which is the sum of its own digits,
    each raised to the power of the number of digits in the given base (base 10).

    :param number: The positive non-zero integer to check.
    :return: True if the number is a Narcissistic number, otherwise False.
    """
    num_str = str(number)
    num_digits = len(num_str)
    return number == sum(int(digit) ** num_digits for digit in num_str)