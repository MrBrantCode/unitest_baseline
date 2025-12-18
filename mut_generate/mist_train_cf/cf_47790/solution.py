"""
QUESTION:
Create a function `str_to_hex(s)` that takes a string `s` and returns its hexadecimal representation. Then, create another function `hex_to_str(h)` that takes a hexadecimal string `h` and returns the original string. The `hex_to_str(h)` function should handle invalid hexadecimal inputs by returning an error message.
"""

def str_to_hex(s):
    res = ''
    for i in s:
        res += hex(ord(i))[2:]
    return res

def hex_to_str(h):
    try:
        byte_arr = bytearray.fromhex(h)
        return byte_arr.decode()
    except (ValueError, TypeError):
        return 'Invalid hexadecimal input'