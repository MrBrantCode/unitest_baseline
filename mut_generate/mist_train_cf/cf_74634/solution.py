"""
QUESTION:
Implement the `XOR_gate` function, which simulates an XOR gate using only NAND gates and AND gates, without using any other type of logic gates. The function should take two Boolean inputs, `a` and `b`, and return their XOR result. You can define additional helper functions, such as `AND_gate` and `NAND_gate`, if necessary. The function should not use any external libraries or classes.
"""

def AND_gate(a, b):
    return a and b

def NAND_gate(a, b):
    return int(not AND_gate(a, b))

def OR_gate(a, b):
    return NAND_gate(NAND_gate(a, a), NAND_gate(b, b))

def XOR_gate(a, b):
    return OR_gate(AND_gate(a, NAND_gate(b, b)), AND_gate(NAND_gate(a, a), b))