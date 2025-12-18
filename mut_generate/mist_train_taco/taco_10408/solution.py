"""
QUESTION:
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.


Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.



Example 1:

Input:
26

Output:
"1a"



Example 2:

Input:
-1

Output:
"ffffffff"
"""

def integer_to_hex(num: int) -> str:
    if num == 0:
        return '0'
    
    # List of hexadecimal characters
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    
    # Handle negative numbers using two's complement
    if num < 0:
        num = (1 << 32) + num
    
    hex_str = []
    while num != 0:
        hex_str.insert(0, hex_chars[num % 16])
        num = num // 16
    
    return ''.join(hex_str)