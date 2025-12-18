"""
QUESTION:
Given a binary string `binary` consisting of only '0' and '1', write a function `maximumBinaryString(binary)` that returns the maximum binary string achievable after performing any number of the following operations:
- If the string contains "00", it can be replaced with "10".
- If the string contains "10", it can be replaced with "01".

The length of `binary` should be within the range 1 <= len(binary) <= 10^5.
"""

def maximumBinaryString(binary):
    zero_count = binary.count('0')
    one_count = binary.count('1')
    if zero_count < 2: return binary 
    return '1'*(one_count+zero_count-1) + '0' + '1'*(len(binary)-one_count-zero_count+1)