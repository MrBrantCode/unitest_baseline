"""
QUESTION:
Implement a `Stack` class with the following methods: `push(item)`, `pop()`, `peek()`, `isEmpty()`, and `size()`, using a list as the underlying data structure. Additionally, implement a function `convertDecToBinary(decimalNo, debug)` that takes a decimal number and a boolean debug flag as input, converts the decimal number to its binary representation using the `Stack` class, and prints the intermediate steps of the conversion process if the debug flag is set to True. The `Stack` class and the `convertDecToBinary` function should be implemented in Python.
"""

def entrance(decimalNo, debug):
    s = []
    temp = decimalNo
    binary_representation = ""
    while temp > 0:
        remainder = temp % 2
        s.append(remainder)
        temp = temp // 2
        if debug:
            print(f"Step {decimalNo-temp}: {temp} -> {remainder}")
    while s:
        binary_representation += str(s.pop())
    return binary_representation