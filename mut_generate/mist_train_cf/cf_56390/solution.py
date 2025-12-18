"""
QUESTION:
Write a function `alphanumericSum` that takes a string of alphanumeric characters as input and returns the sum of their corresponding numeric values, where each uppercase letter is equal to its position in the alphabet (A=1, B=2, ..., Z=26) and each lowercase letter is equal to the negative of its position (a=-1, b=-2, ..., z=-26), and digits are used as their numeric values.
"""

def alphanumericSum(input_string):
    sum_values = 0
    for char in input_string:
        if char.isalpha():
            char_val = ord(char.lower()) - ord('a') + 1
            sum_values += char_val if char.islower() else -char_val
        elif char.isdigit():
            sum_values += int(char)
    return sum_values