"""
QUESTION:
Write a function `apply_logic_gate` that takes a string `op` representing the type of logic gate to be applied ("And", "NAnd", "Or", "NOr", "XOr", "NXOr"), and two integers `height` and `width` representing the size of the grid. The function should return a 2D list representing the grid where each cell contains the result of applying the specified logic gate to the cell's coordinates.
"""

def apply_logic_gate(op, height, width):
    def apply_gate(x, y):
        if op == "And":
            return x and y
        elif op == "NAnd":
            return not (x and y)
        elif op == "Or":
            return x or y
        elif op == "NOr":
            return not (x or y)
        elif op == "XOr":
            return x != y
        elif op == "NXOr":
            return not (x != y)

    grid = [[apply_gate(bool(i % 2), bool(j % 2)) for j in range(width)] for i in range(height)]
    return grid