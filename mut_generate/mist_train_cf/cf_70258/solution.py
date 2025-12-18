"""
QUESTION:
Determine whether an overflow occurs when adding two binary numbers using three numerical representations: two's complement, one's complement, and sign and magnitude. The numbers to be added are 011000 and 011000, and the result should be represented in six bits. Implement a function `check_overflow` to determine if the sum can be accurately represented within the given number of bits.
"""

def check_overflow(sum, num_bits=6):
  return -2**(num_bits-1) <= sum < 2**(num_bits-1)