"""
QUESTION:
Create a function `dec_to_hex(n, case="lower")` that converts a given decimal number `n` to hexadecimal using bitwise operators. The function should take an optional `case` parameter, which defaults to "lower", and return the hexadecimal representation of `n` in either lowercase or uppercase, depending on the value of `case`.
"""

def dec_to_hex(n, case="lower"):
    hex_map = "0123456789abcdef" if case == "lower" else "0123456789ABCDEF"
    hex_num = []
    
    while n != 0:
        rem = n & 15
        hex_num.append(hex_map[rem])
        n >>= 4

    return ''.join(reversed(hex_num))