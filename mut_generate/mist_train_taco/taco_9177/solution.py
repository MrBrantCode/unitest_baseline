"""
QUESTION:
Consider a 32-bit real type with 7 bits from the right as the decimal part, the following 24 bits as the integer part, and the leftmost 1 bit as the sign part as shown below (b1, ..., b32). Represents 0 or 1).

<image>


To translate this format into a decimal representation that is easy for humans to understand, interpret it as follows.
(-1) Sign part × (integer part + decimal part)

In the above expression, the value of the integer part is b8 + 21 x b9 + 22 x b10 + ... + 223 x b31. For example, the integer part is

<image>


If it looks like, the value of the integer part is calculated as follows.
1 + 21 + 23 = 1 + 2 + 8 = 11

On the other hand, the value of the decimal part is (0.5) 1 × b7 ＋ (0.5) 2 × b6 ＋ ... ＋ (0.5) 7 × b1. For example, the decimal part

<image>


If it looks like, the decimal part is calculated as follows.
0.51 + 0.53 = 0.5 + 0.125 = 0.625

Furthermore, in the case of the following bit string that combines the sign part, the integer part, and the decimal part,

<image>


The decimal number represented by the entire bit string is as follows (where -1 to the 0th power is 1).
(-1) 0 × (1 + 2 + 8 + 0.5 + 0.125) = 1 × (11.625) = 11.625


If you enter Q 32-bit bit strings, create a program that outputs the real decimal notation represented by those bit strings without any error.



input

The input consists of one dataset. Input data is given in the following format.


Q
s1
s2
..
..
..
sQ


The number of bit strings Q (1 ≤ Q ≤ 10000) is given in the first row. The input bit string si is given in the following Q row. Suppose the input bit string is given in hexadecimal notation (for example, 0111 1111 1000 1000 0000 0000 0000 0000 is given as 7f880000). In other words, each of the Q lines contains eight hexadecimal numbers, which are 4-bit binary numbers, without any blanks. The table below shows the correspondence between decimal numbers, binary numbers, and hexadecimal numbers.

<image>


Hexadecimal letters a through f are given in lowercase.

output

Outputs the real decimal notation represented by each bit string line by line. However, in the decimal part, if all the digits after a certain digit are 0, the digits after that digit are omitted. As an exception, if the decimal part is 0, one 0 is output to the decimal part.

Example

Input

8
00000000
80000000
00000080
00000040
000000c0
00000100
80000780
80000f70


Output

0.0
-0.0
1.0
0.5
1.5
2.0
-15.0
-30.875
"""

def convert_bit_strings_to_decimals(bit_strings):
    """
    Converts a list of 32-bit hexadecimal bit strings into their corresponding real decimal representations.

    Parameters:
    bit_strings (list of str): A list of 32-bit hexadecimal bit strings.

    Returns:
    list of float: A list of real decimal numbers corresponding to each bit string.
    """
    decimal_numbers = []
    
    for bits in bit_strings:
        bits = f'{int(bits, 16):32b}'
        sign = '-' if bits[0] == '1' else ''
        integer = sum([2 ** i for (i, b) in enumerate(bits[1:25][::-1]) if b == '1'])
        fraction = sum([0.5 ** i for (i, b) in enumerate(bits[25:], start=1) if b == '1'])
        decimal_numbers.append(float(sign + str(integer + fraction)))
    
    return decimal_numbers