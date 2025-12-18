"""
QUESTION:
Create a function named `convert_bin_oct` that takes an array of binary string representations as input. The function should return an array of octal integer equivalents. If a binary string is invalid, the function should return an error message 'Error: Invalid binary number' instead of the octal equivalent. Assume that input array can contain both valid and invalid binary strings.
"""

def convert_bin_oct(arr):
    res = []
    for bin_str in arr:
        try:
            res.append(oct(int(bin_str, 2)))
        except ValueError:
            res.append('Error: Invalid binary number')
    return res