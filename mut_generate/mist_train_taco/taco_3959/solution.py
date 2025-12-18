"""
QUESTION:
Polycarp has just invented a new binary protocol for data transmission. He is encoding positive integer decimal number to binary string using following algorithm:

  Each digit is represented with number of '1' characters equal to the value of that digit (for 0 it is zero ones).  Digits are written one by one in order corresponding to number and separated by single '0' character. 

Though Polycarp learnt how to encode the numbers, he has no idea how to decode them back. Help him calculate the decoded number.


-----Input-----

The first line contains one integer number n (1 ≤ n ≤ 89) — length of the string s.

The second line contains string s — sequence of '0' and '1' characters, number in its encoded format. It is guaranteed that the number corresponding to the string is positive and doesn't exceed 10^9. The string always starts with '1'.


-----Output-----

Print the decoded number.


-----Examples-----
Input
3
111

Output
3

Input
9
110011101

Output
2031
"""

def decode_binary_protocol(n: int, s: str) -> str:
    """
    Decodes a binary protocol string back to its original decimal number.

    Parameters:
    n (int): The length of the encoded string.
    s (str): The encoded string consisting of '1's and '0's.

    Returns:
    str: The decoded decimal number as a string.
    """
    result = ''
    counter = 0
    for i in range(len(s)):
        if s[i - 1] == '0' and s[i] == '0':
            if counter > 0:
                result += str(counter)
                counter = 0
            result += '0'
            continue
        if s[i] == '1':
            counter += 1
        elif s[i] == '0':
            if counter > 0:
                result += str(counter)
            counter = 0
    result += str(counter)
    return result