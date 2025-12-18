"""
QUESTION:
Create a function named `create_pyramid` that takes a positive integer `n`, a sequence type (`'consecutive'` or `'square'`), and an optional quantity of extra blocks (`extra`, default is 0). The function should generate a pyramid with `n` layers, where each layer's block count depends on the sequence type and the previous layer's block count. For `'consecutive'`, add the next consecutive integer to the previous layer's block count, and for `'square'`, add the next perfect square to the previous block count. The initial layer should have `n` blocks, with the option to add extra blocks. Return the block counts list for each layer.
"""

def create_pyramid(n, sequence, extra=0):
    blocks = [n + extra]
    for i in range(1, n):
        if sequence == 'consecutive':
            blocks.append(blocks[-1] + i + 1)
        elif sequence == 'square':
            blocks.append(blocks[-1] + (i + 1)**2)
    return blocks