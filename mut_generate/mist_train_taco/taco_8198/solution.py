"""
QUESTION:
AtCoDeer the deer has found two positive integers, a and b.
Determine whether the concatenation of a and b in this order is a square number.

-----Constraints-----
 - 1 ≤ a,b ≤ 100
 - a and b are integers.

-----Input-----
Input is given from Standard Input in the following format:
a b

-----Output-----
If the concatenation of a and b in this order is a square number, print Yes; otherwise, print No.

-----Sample Input-----
1 21

-----Sample Output-----
Yes

As 121 = 11 × 11, it is a square number.
"""

import math

def is_concatenation_square(a: int, b: int) -> str:
    # Concatenate a and b as strings and convert to integer
    concatenated_number = int(f"{a}{b}")
    
    # Calculate the square root of the concatenated number
    sqrt_value = int(math.sqrt(concatenated_number))
    
    # Check if the square of the square root equals the concatenated number
    if sqrt_value * sqrt_value == concatenated_number:
        return 'Yes'
    else:
        return 'No'