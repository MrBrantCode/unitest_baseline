"""
QUESTION:
-----Input-----

The input contains a single integer $a$ ($0 \le a \le 63$).


-----Output-----

Output a single number.


-----Examples-----
Input
2

Output
2

Input
5

Output
24

Input
35

Output
50
"""

import math

def transform_binary_representation(a: int) -> int:
    if a == 0:
        return 0
    
    # Convert the number to binary and pad with leading zeros to ensure it has 6 bits
    binary_str = bin(a).replace('0b', '').zfill(6)
    
    # Convert the binary string to a list of characters for easy swapping
    binary_list = list(binary_str)
    
    # Perform the specified swaps
    (binary_list[1], binary_list[5]) = (binary_list[5], binary_list[1])
    (binary_list[2], binary_list[3]) = (binary_list[3], binary_list[2])
    
    # Convert the modified binary list back to an integer
    transformed_value = int(''.join(binary_list), 2)
    
    return transformed_value