"""
QUESTION:
Create a function named `check_sequence` that takes two string parameters, `num_str1` and `num_str2`, both containing numerical digits. The function should return `True` if the sequence of digits in `num_str2` is maintained in `num_str1`, and `False` otherwise. The function should only consider the order of digits in `num_str1` and ignore any other characters.
"""

def check_sequence(num_str1, num_str2):
    last_index = 0
    for digit in num_str2:
        if digit in num_str1[last_index:]:
            last_index = num_str1.index(digit, last_index) + 1
        else:
            return False
    return True