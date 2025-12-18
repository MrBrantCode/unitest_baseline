"""
QUESTION:
Write a function called `swap_blocks` that takes a string `s` as input and returns the modified string where the first and second blocks of characters are swapped. A block is defined as a continuous sequence of the same character type (alpha, digit, special character). If the string does not have at least two different character blocks, return the original string. The function should only swap the first two blocks, even if the string has more than two blocks.
"""

import re

def swap_blocks(s):
    # Divide the string into blocks
    blocks = re.findall(r'\D+|\d+|\W+', s)

    # If there are less than two blocks, return the original string
    if len(blocks) < 2:
        return s

    # Swap the first two blocks
    blocks[0], blocks[1] = blocks[1], blocks[0]

    # Join the blocks back together into a string
    return ''.join(blocks)