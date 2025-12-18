"""
QUESTION:
Determine the function get_XOR_prime(index) that returns the index-th XOR-prime, where XOR-prime is an integer exceeding 1 that cannot be expressed as an XOR-multiplication of two integers larger than 1. The function should not actually perform the XOR-multiplication to avoid excessive CPU time and should handle numbers of arbitrary size.
"""

def get_XOR_prime(index):
    power_of_two_minus_one = index - 1
    prime = ((3 << power_of_two_minus_one) | (3 >> (31 - power_of_two_minus_one))) & 0xFFFFFFFF
    return prime