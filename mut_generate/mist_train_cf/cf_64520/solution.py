"""
QUESTION:
Write a function to convert a float to a WCHAR string with two decimal places using wsprintf. The function should take a float as input and return a WCHAR string. The function must use wsprintf or an equivalent standardized function like swprintf.
"""

def float_to_wchar_string(value):
    return "{:.2f}".format(value)