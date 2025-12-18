"""
QUESTION:
-----Input-----

The input contains a single integer a (0 ≤ a ≤ 35).


-----Output-----

Output a single integer.


-----Examples-----
Input
3

Output
8

Input
10

Output
1024
"""

def swap_bits_and_convert(a: int) -> int:
    # Convert the integer to a 6-bit binary string
    binary_str = bin(a)[2:].zfill(6)
    
    # Convert the binary string to a list of characters
    n = list(binary_str)
    
    # Perform the bit-swapping operations
    n[1], n[5] = n[5], n[1]
    n[2], n[3] = n[3], n[2]
    
    # Convert the modified binary string back to an integer
    result = int(''.join(n), 2)
    
    return result