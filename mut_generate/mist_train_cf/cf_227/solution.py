"""
QUESTION:
Create a function `square_hex_reverse` that takes a list of integers as input and returns a list of strings. For each integer in the input list, square the integer, convert it to hexadecimal, and reverse the hexadecimal string. If the squared integer is a perfect square (i.e., its square root is an integer), reverse the hexadecimal string an additional time.
"""

def square_hex_reverse(lst):
    result = []
    for num in lst:
        square = num ** 2
        hex_str = hex(square)[2:]
        if int(hex_str, 16) ** 0.5 == int(int(hex_str, 16) ** 0.5): 
            hex_str = hex_str[::-1][::-1] 
        else:
            hex_str = hex_str[::-1]
        result.append(hex_str)
    return result