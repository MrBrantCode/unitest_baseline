"""
QUESTION:
Implement the `untemper` function that takes a 32-bit integer `v` as input and returns the original untempered random number. The input `v` has been tempered by a series of bitwise operations, specifically: 
- right shift by 18 bits and XOR operation
- left shift by 15 bits, AND operation with mask 0xefc60000, and XOR operation
- left shift by 7 bits, AND operation with mask 0x9d2c5680, and XOR operation
- right shift by 11 bits and XOR operation

Reverse these operations to recover the original untempered random number.
"""

def untemper(v):
    """ Reverses the tempering which is applied to outputs of MT19937 """
    v = untemper_right_shift_xor(v, 18)
    v = untemper_left_shift_and_xor(v, 15, 0xefc60000)
    v = untemper_left_shift_and_xor(v, 7, 0x9d2c5680)
    v = untemper_right_shift_xor(v, 11)
    return v

def untemper_right_shift_xor(v, shift):
    mask = (1 << shift) - 1
    result = v
    for i in range(31, -1, -1):
        result = v ^ (result >> shift) if i > 0 else result
        v = v ^ (result >> shift) if i > 0 else v
    return result

def untemper_left_shift_and_xor(v, shift, mask):
    result = v
    for i in range(32):
        result = v ^ ((result << shift) & mask) if i > 0 else result
        v = v ^ ((result << shift) & mask) if i > 0 else v
    return result