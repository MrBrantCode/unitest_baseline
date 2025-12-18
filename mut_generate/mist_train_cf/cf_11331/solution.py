"""
QUESTION:
Write a function `is_valid_ipv4(address)` that checks if a given string is a valid IPv4 address. 

The function should return `True` if the string is a valid IPv4 address and `False` otherwise. A valid IPv4 address consists of four decimal numbers, separated by periods, where each decimal number is between 0 and 255. Leading zeros are not allowed. The function should also handle edge cases where the string is empty, contains characters other than digits and periods, or has more or less than four decimal numbers.
"""

def is_valid_ipv4(address):
    if len(address) == 0:
        return False

    nums = address.split(".")
    if len(nums) != 4:
        return False

    for num in nums:
        if not num.isdigit():
            return False

        if num[0] == "0" and len(num) > 1:
            return False

        if int(num) > 255:
            return False

    return True