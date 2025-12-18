"""
QUESTION:
Many people are aware of DMCA – Digital Millennium Copyright Act. But another recently proposed DMCA – Digital Millennium Calculation Act – is much less known.

In this problem you need to find a root of a number according to this new DMCA law.

Input

The input contains a single integer a (1 ≤ a ≤ 1000000).

Output

Output the result – an integer number.

Examples

Input


1


Output


1


Input


81


Output


9
"""

def calculate_dmca_root(a: int) -> int:
    sumo = a
    while a >= 10:
        sumo = 0
        while a != 0:
            sumo += a % 10
            a //= 10
        a = sumo
    return sumo