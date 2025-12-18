"""
QUESTION:
Alex, Bob, and, Chef are standing on the coordinate plane. Chef is standing at the origin (coordinates (0, 0)) while the location of Alex and Bob are (X_{1}, Y_{1}) and (X_{2}, Y_{2}) respectively.

Amongst Alex and Bob, find out who is at a farther distance from Chef or determine if both are at the same distance from Chef.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The first and only line of each test case contains four space-separated integers X_{1}, Y_{1}, X_{2}, and Y_{2} — the coordinates of Alex and Bob.

------ Output Format ------ 

For each test case, output on a new line:
- ALEX, if Alex is at a farther distance from Chef.
- BOB, if Bob is at a farther distance from Chef.
- EQUAL, if both are standing at the same distance from Chef.

You may print each character in uppercase or lowercase. For example, Bob, BOB, bob, and bOB, are all considered identical.

------ Constraints ------ 

$1 ≤ T ≤ 2000$
$-1000 ≤ X_{1}, Y_{1}, X_{2}, Y_{2} ≤ 1000$

----- Sample Input 1 ------ 
3
-1 0 3 4
3 4 -4 -3
8 -6 0 5

----- Sample Output 1 ------ 
BOB
EQUAL
ALEX
----- explanation 1 ------ 
Test case $1$: Alex is at a distance $1$ from Chef while Bob is at distance $5$ from Chef. Thus, Bob is at a farther distance.

Test case $2$: Alex is at a distance $5$ from Chef and Bob is also at distance $5$ from Chef. Thus, both are at the same distance.

Test case $3$: Alex is at a distance $10$ from Chef while Bob is at distance $5$ from Chef. Thus, Alex is at a farther distance.
"""

import math

def compare_distances(test_cases):
    results = []
    for (x1, y1, x2, y2) in test_cases:
        d1 = math.sqrt(x1 ** 2 + y1 ** 2)
        d2 = math.sqrt(x2 ** 2 + y2 ** 2)
        if d1 == d2:
            results.append('EQUAL')
        elif d1 > d2:
            results.append('ALEX')
        else:
            results.append('BOB')
    return results