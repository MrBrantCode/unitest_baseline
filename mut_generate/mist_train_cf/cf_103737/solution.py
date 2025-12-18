"""
QUESTION:
Write a function named `remove_trailing_zeros` that takes a float number as input, removes all trailing zeros after the decimal point, and returns the resulting number as a string. The function should have a time complexity of O(n), where n is the number of digits in the given float number, and should not use any built-in functions or libraries to achieve the desired result.
"""

def remove_trailing_zeros(num):
    num_str = str(num)
    result = ""
    for i in range(len(num_str) - 1, -1, -1):
        if num_str[i] == "0" and not result:
            continue
        result += num_str[i]
    return result[::-1]