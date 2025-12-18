"""
QUESTION:
Create a function called `hash_data` that implements a 32-bit hash for a given 32-bit unsigned integer data using only bitwise operators. The hash function should split the data into four 8-bit parts, perform bitwise operations on these parts, and combine the results back into a 32-bit hash value. The input data is a 32-bit unsigned integer. The function should return the resulting 32-bit hash value.
"""

def hash_data(data):
    # Split the 32-bit data into four 8-bit parts
    part1 = (data & 0xFF000000) >> 24
    part2 = (data & 0x00FF0000) >> 16
    part3 = (data & 0x0000FF00) >> 8
    part4 = data & 0x000000FF

    # Perform bitwise operations on the parts
    part1 = (part1 ^ part2) << 1
    part2 = (part2 ^ part3) << 2
    part3 = (part3 ^ part4) << 3
    part4 = (part4 ^ part1) << 4

    # Combine the parts back into a 32-bit hash
    hash_value = (part1 << 24) | (part2 << 16) | (part3 << 8) | part4

    return hash_value