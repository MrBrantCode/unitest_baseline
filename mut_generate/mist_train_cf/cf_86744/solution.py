"""
QUESTION:
Implement a function `count_unique_digits(num)` to calculate the total number of unique digits in a number. The number can be positive or negative, and the negative sign is considered as a digit. The function should have a time complexity of O(n), where n is the number of digits in the input number.
"""

def count_unique_digits(num):
    digits = set()  # Initialize an empty set to store unique digits
    num = str(num)  # Convert the number to a string
    
    for digit in num:
        if digit != '-':  # Ignore the negative sign
            digits.add(digit)
    
    return len(digits)