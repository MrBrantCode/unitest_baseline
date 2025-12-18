"""
QUESTION:
Robbers, who attacked the Gerda's cab, are very successful in covering from the kingdom police. To make the goal of catching them even harder, they use their own watches.

First, as they know that kingdom police is bad at math, robbers use the positional numeral system with base 7. Second, they divide one day in n hours, and each hour in m minutes. Personal watches of each robber are divided in two parts: first of them has the smallest possible number of places that is necessary to display any integer from 0 to n - 1, while the second has the smallest possible number of places that is necessary to display any integer from 0 to m - 1. Finally, if some value of hours or minutes can be displayed using less number of places in base 7 than this watches have, the required number of zeroes is added at the beginning of notation.

Note that to display number 0 section of the watches is required to have at least one place.

Little robber wants to know the number of moments of time (particular values of hours and minutes), such that all digits displayed on the watches are distinct. Help her calculate this number.

Input

The first line of the input contains two integers, given in the decimal notation, n and m (1 ≤ n, m ≤ 109) — the number of hours in one day and the number of minutes in one hour, respectively.

Output

Print one integer in decimal notation — the number of different pairs of hour and minute, such that all digits displayed on the watches are distinct.

Examples

Input

2 3


Output

4


Input

8 2


Output

5

Note

In the first sample, possible pairs are: (0: 1), (0: 2), (1: 0), (1: 2).

In the second sample, possible pairs are: (02: 1), (03: 1), (04: 1), (05: 1), (06: 1).
"""

from itertools import permutations, combinations

def count_distinct_time_pairs(n, m):
    # Calculate the number of places needed to represent hours and minutes in base 7
    p1 = 0
    x1 = 1
    while x1 <= n - 1:
        x1 *= 7
        p1 += 1
    
    p2 = 0
    x2 = 1
    while x2 <= m - 1:
        x2 *= 7
        p2 += 1
    
    # Ensure at least one place is used for both hours and minutes
    p1 = max(p1, 1)
    p2 = max(p2, 1)
    
    # Total length of digits needed
    Len = p1 + p2
    
    # Count valid pairs
    cnt = 0
    for comb in combinations([0, 1, 2, 3, 4, 5, 6], Len):
        for perm in permutations(comb):
            a = b = 0
            p = 1
            for k in range(p1 - 1, -1, -1):
                a += perm[k] * p
                p *= 7
            p = 1
            for k in range(Len - 1, p1 - 1, -1):
                b += perm[k] * p
                p *= 7
            if a >= n or b >= m:
                continue
            if perm:
                cnt += 1
    
    return cnt