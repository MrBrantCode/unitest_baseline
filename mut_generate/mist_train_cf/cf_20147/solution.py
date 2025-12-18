"""
QUESTION:
Implement a function `five_input_and_gate` using NAND gates, with the following constraints:
- The function should implement a five-input AND gate.
- The function should use only NAND gates.
- The function should have a minimum number of gates.
- The function should have a maximum propagation delay of 1 nanosecond.
- The function should consume a maximum of 1 milliwatt of power.
- The function should have a fan-out of at least 10.
"""

def five_input_and_gate(a, b, c, d, e):
    # First NAND gate
    nand_1 = not (a and b)
    
    # Second NAND gate
    nand_2 = not (c and d)
    
    # Third NAND gate
    nand_3 = not (nand_1 and nand_2 and e)
    
    # Invert the output to get AND gate output
    return not nand_3