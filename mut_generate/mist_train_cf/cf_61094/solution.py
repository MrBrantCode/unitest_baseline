"""
QUESTION:
Design a function called `binary_to_decimal_sum` that takes a list of binary numerals as strings. The function should convert each binary numeral to its decimal equivalent and return the sum of all unique decimal values.
"""

def binary_to_decimal_sum(bin_list):
    return sum(set(int(bin_num, 2) for bin_num in bin_list))