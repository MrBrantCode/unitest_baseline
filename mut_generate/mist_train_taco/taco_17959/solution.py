"""
QUESTION:
Description
You are given a function f: WxW → W, where W represents the set of whole numbers.

The following data is given to you:
f(4,3)=7
f(7,8)=15
f(9,16)=25
f(10,177)=187
f(49,76)=125
f(160,257)=417
f(165,10)=175
f(178,213)=103
f(197,2)=199
f(199,296)=495
f(1000,19)=1019
f(1004,19)=1023

Write a program which calculates f(x, y) given input of two natural numbers.

Input Format
One line containing two space separated integers x and y

Output Format
One line containing the result of f(x, y)

Input Limits
0 < x, y < 10^11

SAMPLE INPUT
1004 19

SAMPLE OUTPUT
1023

Explanation

No explanantion
"""

def calculate_f(x: int, y: int) -> int:
    """
    Calculates the function f(x, y) which is defined as the bitwise XOR of x and y.

    Parameters:
    x (int): The first input integer.
    y (int): The second input integer.

    Returns:
    int: The result of f(x, y), which is x XOR y.
    """
    return x ^ y