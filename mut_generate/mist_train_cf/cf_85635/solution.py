"""
QUESTION:
Write a function `isValidIMEI` that checks whether a given string represents a valid International Mobile Equipment Identity (IMEI) number. The IMEI number should consist of exactly 15 digits and pass the Luhn check. The function should return `True` if the IMEI number is valid and `False` otherwise.
"""

def isValidIMEI(IMEI):
    if len(IMEI)!=15 or not IMEI.isdigit():
        return False
    sum, flag = 0, False
    for digit in reversed(IMEI):
        digit = int(digit)
        if flag:
            digit <<= 1
            if digit > 9:
                digit -= 9
        sum += digit
        flag = not flag
    return sum % 10 == 0