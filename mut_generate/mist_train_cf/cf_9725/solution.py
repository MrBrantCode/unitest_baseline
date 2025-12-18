"""
QUESTION:
Implement a function called `four_bit_adder` that takes two 4-bit binary numbers, A and B, and returns their sum as a 4-bit or 5-bit binary number (depending on the occurrence of overflow), implemented using only NAND gates. The function should not use any external libraries and should only use the basic logical operators.
"""

def four_bit_adder(a, b):
    def nand(x, y):
        return int(not (x and y))

    def and_gate(x, y):
        return nand(nand(x, y), nand(x, y))

    def or_gate(x, y):
        return nand(nand(x, x), nand(y, y))

    def not_gate(x):
        return nand(x, x)

    def xor_gate(x, y):
        return and_gate(or_gate(x, y), nand(x, y))

    def half_adder(a, b):
        sum_bit = xor_gate(a, b)
        carry_bit = and_gate(a, b)
        return sum_bit, carry_bit

    def full_adder(a, b, cin):
        sum1, carry1 = half_adder(a, b)
        sum_bit, carry2 = half_adder(sum1, cin)
        carry_bit = or_gate(carry1, carry2)
        return sum_bit, carry_bit

    # Initialize the inputs
    a_bits = [(a >> i) & 1 for i in range(4)]
    a_bits = a_bits[::-1]
    b_bits = [(b >> i) & 1 for i in range(4)]
    b_bits = b_bits[::-1]

    # Initialize the carry-in bit
    cin = 0

    # Initialize the output
    output = ""

    # Perform the addition
    for i in range(4):
        sum_bit, cin = full_adder(a_bits[i], b_bits[i], cin)
        output = str(sum_bit) + output

    # Check for overflow
    if cin == 1:
        output = str(cin) + output

    # Convert the output to an integer
    output = int(output, 2)

    return output