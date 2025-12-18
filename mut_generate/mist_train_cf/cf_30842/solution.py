"""
QUESTION:
Implement a function `_bit_reconstruction_and_f` that takes an optional boolean parameter `xor_x4` with a default value of `False`. The function should perform the following operations: calculate `w_` as the result of the bitwise AND operation between the XOR of `_get_h_l(15, 14)` and `r1` added to `r2`, followed by bitwise AND with `_2_power_32_minus_1`. It should also calculate `w1` as the result of adding `r1` to the value returned by `_get_l_h(11, 9)`. If `xor_x4` is `True`, `w_` should be XORed with `4`. The function should return a reconstructed 32-bit integer. Assume access to variables `lfsr`, `lfsr_curr_ptr`, `r1`, `r2`, and functions `_lfsr`, `_get_h_l`, `_get_l_h` with their respective implementations.
"""

from typing import Union

def bit_reconstruction_and_f(xor_x4=False) -> Union[int, None]:
    w_ = ((_get_h_l(15, 14) ^ r1) + r2) & _2_power_32_minus_1

    if xor_x4:
        w_ ^= 0x4  # XOR with 4 if xor_x4 is True

    w1 = (r1 + _get_l_h(11, 9)) & _2_power_32_minus_1  # Ensure result is 32-bit

    return ((_lfsr(l_index) & _low_bitmask) << 16) | ((_lfsr(h_index) & _high_bitmask) >> 15)  # Reconstruct 32-bit integer