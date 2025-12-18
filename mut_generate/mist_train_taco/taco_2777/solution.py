"""
QUESTION:
The smallest unit of data handled by a computer is called a bit, and the amount of information that represents multiple bits together is called a word. Currently, many computers process one word as 32 bits.

For a computer that represents one word in 32 bits, create a program that outputs the amount of data W given in word units in bit units.



Input

The input is given in the following format.


W


The input consists of one line and is given the amount of data W (0 ≤ W ≤ 100).

Output

Outputs the bitwise value on one line.

Examples

Input

4


Output

128


Input

3


Output

96
"""

def convert_words_to_bits(W: int) -> int:
    """
    Converts the amount of data given in word units to bit units for a 32-bit word system.

    Parameters:
    W (int): The amount of data in word units.

    Returns:
    int: The amount of data in bit units.
    """
    return W * 32