"""
QUESTION:
Create a function called `xor_gate` that takes two inputs, `A` and `B`, and returns the result of the XOR operation between `A` and `B` using only NAND and NOT gates.
"""

def xor_gate(A, B):
    def nand_gate(a, b):
        return ~(a & b)

    def not_gate(a):
        return nand_gate(a, a)

    def and_gate(a, b):
        return not_gate(nand_gate(a, not_gate(nand_gate(b, b))))

    def or_gate(a, b):
        return nand_gate(not_gate(nand_gate(a, b)), not_gate(nand_gate(a, b)))

    return or_gate(and_gate(A, not_gate(B)), and_gate(not_gate(A), B))