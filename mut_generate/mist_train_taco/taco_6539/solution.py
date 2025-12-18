"""
QUESTION:
There is a huge blanket on your bed but unfortunately it has N stains. You cover them using 
a single, rectangular silk cloth. The silk is expensive, which is why the rectangular piece needs to have the least area as possible. You love this blanket and decide to minimize the area covering the  stains. You buy some cleaning liquid to remove the stains but sadly it isn't enough to clean all of them. You can just remove exactly K stains. The rest of the stains need to be covered using a single, rectangular fragment of silk cloth.

Let X denote the area of the smallest possible silk cloth that may cover all the stains originally. You need to find the number of different ways in which you may remove K stains so that the remaining N-K stains can be covered with silk of area strictly less than X (We are looking for any configuration that will reduce the cost).

Assume that each stain is a point and that the rectangle is aligned parallel to the axes.  

Input Format

The first line contains two integers N (1<=N<=1000) and K (0<=K<=N). 
Next follow N lines, one for each stain. Each line contains two integers in the form 'X Y', (0<=X,Y<100000), the coordinates of each stain into the blanket. Each pair of coordinates is unique.

Output Format

Output a single integer. The remainder of the division by 1000000007 of the answer.

Sample Input
5 2
0 1
3 3
2 0
0 3
2 3

Sample Output
8

Explanation

We can clean two spots. So removing any of the following set of stains will lead us to a conbination that will need less amount of silk.(The numbers refer to the indices of the stains in the input and they begin from 1).

1, 4
2, 1
2, 3
2, 4
2, 5
3, 1
3, 4
3, 5

So there are 8 ways.
"""

from itertools import combinations
from functools import reduce

def stain_combos(n, k):
    p = 1000000007
    if k < 0:
        return 0
    out = 1
    for i in range(n - k + 1, n + 1):
        out = out * i % p
    denom = 1
    for i in range(1, k + 1):
        denom = denom * i % p
    denom = pow(denom, p - 2, p)
    return out * denom % p

def calculate_minimum_silk_area_ways(n, k, stains):
    min_x = min(stain[0] for stain in stains)
    max_x = max(stain[0] for stain in stains)
    min_y = min(stain[1] for stain in stains)
    max_y = max(stain[1] for stain in stains)
    
    top = {stain for stain in stains if stain[0] == min_x}
    bot = {stain for stain in stains if stain[0] == max_x}
    left = {stain for stain in stains if stain[1] == min_y}
    right = {stain for stain in stains if stain[1] == max_y}
    
    out = 0
    for i in range(1, 5):
        for sides in combinations([top, bot, left, right], i):
            removed = reduce(lambda x, y: x.union(y), sides)
            length = len(removed)
            out += (-1) ** (i + 1) * stain_combos(len(stains) - length, k - length)
    
    return out % 1000000007