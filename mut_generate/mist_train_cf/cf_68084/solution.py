"""
QUESTION:
Write a function named binary_NOR that takes two integers x and y as inputs and returns their binary NOR operation as a binary string. The function should convert the integers to their binary representations, ensure they have the same length by padding zeros to the left if necessary, and then perform the binary NOR operation on the corresponding bits. The function should return the result as a binary string.
"""

def binary_NOR(x, y):
    binary_x = bin(x)[2:]
    binary_y = bin(y)[2:]

    while len(binary_x) > len(binary_y):
        binary_y = '0' + binary_y
    while len(binary_x) < len(binary_y):
        binary_x = '0' + binary_x

    nor = ''
    for b1, b2 in zip(binary_x, binary_y):
        nor += '1' if b1=='0' and b2=='0' else '0'

    return nor