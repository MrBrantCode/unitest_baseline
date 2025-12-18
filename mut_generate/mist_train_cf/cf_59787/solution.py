"""
QUESTION:
Write a function `convert_to_int` that takes a list of alphanumeric strings as input and returns a list of integers. The function should extract the digits from each string and convert them to integers. The input list may contain strings with leading, trailing, or embedded non-digit characters. The function should not handle errors for strings containing no digits, assuming each string has at least one digit.
"""

def convert_to_int(str_list):
    digits_list = [''.join(filter(str.isdigit, i)) for i in str_list]
    return [int(i) for i in digits_list]