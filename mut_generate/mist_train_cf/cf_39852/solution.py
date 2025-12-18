"""
QUESTION:
Implement the `reducing` function, which takes a binary operation (`op`) and one or more operands. The binary operation can be either a function or a string representing a method to be called on the operands. The function should apply the operation iteratively to the operands, handling both list-based and non-list-based operations. If the binary operation is a function, apply it iteratively to the operands. If the binary operation is a string, treat it as a method name and call it on the operands.
"""

from functools import reduce
from operator import add

def reducing(op, *operands):
    if isinstance(operands[0], list):  
        if callable(op):  
            return reduce(op, operands[0])
        else:  
            return reduce(getattr(operands[0][0], op), operands[0])
    else:  
        if callable(op):  
            return reduce(op, operands)
        else:  
            return reduce(getattr(operands[0], op), operands)