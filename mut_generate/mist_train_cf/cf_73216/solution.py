"""
QUESTION:
Implement the function `validate_and_xor_alternating_subseq` that takes two binary strings `a` and `b` as input. The function should first validate if the input strings are of equal length. If they are, perform a binary XOR operation on the strings, find the longest alternating subsequence in the result, and return it as a string. If the strings are not of equal length, return the error message "Error: Strings are of different lengths." An alternating subsequence is a subsequence where no two adjacent elements are the same.
"""

from typing import Union

def validate_and_xor_alternating_subseq(a: str, b: str) -> Union[str, None]:
    if len(a) != len(b):
        return "Error: Strings are of different lengths."

    xor_result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    alt_subseq = xor_result[0]
    for i in range(1, len(xor_result)):
        if xor_result[i] != alt_subseq[-1]:
            alt_subseq += xor_result[i]
    return alt_subseq