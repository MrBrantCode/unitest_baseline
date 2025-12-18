"""
QUESTION:
Given two non-negative decimal integers $a$ and $b$, calculate their AND (logical conjunction), OR (logical disjunction) and XOR (exclusive disjunction) and print them in binary representation of 32 bits.

Constraints

* $0 \leq a, b \leq 2^{32} - 1$

Input

The input is given in the following format.


$a \; b$


Output

Print results of AND, OR and XOR in a line respectively.

Example

Input

8 10


Output

00000000000000000000000000001000
00000000000000000000000000001010
00000000000000000000000000000010
"""

def calculate_bitwise_operations(a: int, b: int) -> tuple:
    """
    Calculate the AND, OR, and XOR of two non-negative decimal integers and return their 32-bit binary representations.

    Parameters:
    a (int): The first non-negative decimal integer.
    b (int): The second non-negative decimal integer.

    Returns:
    tuple: A tuple containing three strings representing the 32-bit binary representations of AND, OR, and XOR results respectively.
    """
    and_result = '{:032b}'.format(a & b)
    or_result = '{:032b}'.format(a | b)
    xor_result = '{:032b}'.format(a ^ b)
    
    return (and_result, or_result, xor_result)