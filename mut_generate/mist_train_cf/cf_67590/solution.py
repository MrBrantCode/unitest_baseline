"""
QUESTION:
Implement the function `XNOR_GATE` that takes two boolean inputs `x` and `y` and returns their XNOR (equivalence gate) using only three NOR gates. The XNOR gate outputs true or "1" only when the number of true inputs is even.
"""

def XNOR_GATE(x, y):
    def NOR(a, b):
        if a == 0 and b == 0:
            return 1
        else:
            return 0

    nor1 = NOR(x, y)
    nor2 = NOR(x, nor1)
    nor3 = NOR(y, nor1)
    xnor = NOR(nor2, nor3)
    return xnor