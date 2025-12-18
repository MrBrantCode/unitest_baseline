"""
QUESTION:
Gerald is setting the New Year table. The table has the form of a circle; its radius equals R. Gerald invited many guests and is concerned whether the table has enough space for plates for all those guests. Consider all plates to be round and have the same radii that equal r. Each plate must be completely inside the table and must touch the edge of the table. Of course, the plates must not intersect, but they can touch each other. Help Gerald determine whether the table is large enough for n plates.

Input

The first line contains three integers n, R and r (1 ≤ n ≤ 100, 1 ≤ r, R ≤ 1000) — the number of plates, the radius of the table and the plates' radius.

Output

Print "YES" (without the quotes) if it is possible to place n plates on the table by the rules given above. If it is impossible, print "NO".

Remember, that each plate must touch the edge of the table. 

Examples

Input

4 10 4


Output

YES


Input

5 10 4


Output

NO


Input

1 10 10


Output

YES

Note

The possible arrangement of the plates for the first sample is: 

<image>
"""

import math

def can_place_plates(n: int, R: int, r: int) -> str:
    if r > R:
        return 'NO'
    if 2 * r > R:
        if n > 1:
            return 'NO'
        else:
            return 'YES'
    z = 2 * n * math.asin(r / (R - r))
    if z > 2 * math.pi + 1e-10:
        return 'NO'
    else:
        return 'YES'