"""
QUESTION:
Create a function named `XOR` that takes two inputs and returns True if either, but not both, inputs are true, and False otherwise. The function should utilize a combination of the `NAND` function, which yields False only when both inputs are true, and the `NOT` function, which reverses the input value. However, the XOR gate cannot be constructed using only two NAND gates and one NOT gate.
"""

def XOR(a, b):
    def NAND(x, y):
        return not (x and y)

    return NAND(NAND(a, NAND(a,b)), NAND(b, NAND(a,b)))