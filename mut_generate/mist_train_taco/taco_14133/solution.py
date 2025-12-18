"""
QUESTION:
Programmers' kids solve this riddle in 5-10 minutes. How fast can you do it?


-----Input-----

The input contains a single integer n (0 ≤ n ≤ 2000000000).


-----Output-----

Output a single integer.


-----Examples-----
Input
11

Output
2

Input
14

Output
0

Input
61441

Output
2

Input
571576

Output
10

Input
2128506

Output
3
"""

def count_hex_holes(n: int) -> int:
    # Dictionary mapping each hex digit to the number of holes it contains
    val = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1, 'a': 1, 'b': 2, 'c': 0, 'd': 1, 'e': 0, 'f': 0}
    
    # Convert the integer to its hexadecimal representation and strip the '0x' prefix
    hex_str = hex(n)[2:]
    
    # Initialize the answer to 0
    ans = 0
    
    # Sum the number of holes for each character in the hexadecimal string
    for c in hex_str:
        ans += val[c]
    
    return ans