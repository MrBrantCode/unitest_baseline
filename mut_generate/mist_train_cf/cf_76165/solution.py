"""
QUESTION:
Create a function named `binary_group` that takes two parameters, N and M, where 1 <= N <= 10^5 and 0 <= M <= 10^10. The function should convert M into an 8-bit binary representation, pad the binary string with leading zeros to make its length divisible by N, split the binary string into groups of size N, and return the groups separated by a space.
"""

def binary_group(N, M):
    bin_str = format(M, '08b')

    while len(bin_str) % N != 0:
        bin_str = '0' + bin_str

    return ' '.join([bin_str[i:i+N] for i in range(0, len(bin_str), N)])