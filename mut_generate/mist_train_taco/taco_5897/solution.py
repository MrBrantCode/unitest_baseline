"""
QUESTION:
AtCoDeer the deer has N square tiles. The tiles are numbered 1 through N, and the number given to each tile is written on one side of the tile. Also, each corner of each tile is painted in one of the 1000 colors, which are represented by the integers 0 between 999. The top-left, top-right, bottom-right and bottom-left corner of the tile with the number i are painted in color C_{i,0}, C_{i,1}, C_{i,2} and C_{i,3}, respectively, when seen in the direction of the number written on the tile (See Figure 1).
Figure 1: The correspondence between the colors of a tile and the input
AtCoDeer is constructing a cube using six of these tiles, under the following conditions:
 - For each tile, the side with the number must face outward.
 - For each vertex of the cube, the three corners of the tiles that forms it must all be painted in the same color.
Help him by finding the number of the different cubes that can be constructed under the conditions.
Since each tile has a number written on it, two cubes are considered different if the set of the used tiles are different, or the tiles are used in different directions, even if the formation of the colors are the same. (Each tile can be used in one of the four directions, obtained by 90° rotations.) Two cubes are considered the same only if rotating one in the three dimensional space can obtain an exact copy of the other, including the directions of the tiles.
Figure 2: The four directions of a tile

-----Constraints-----
 - 6≦N≦400
 - 0≦C_{i,j}≦999 (1≦i≦N , 0≦j≦3)

-----Input-----
The input is given from Standard Input in the following format:
N
C_{1,0} C_{1,1} C_{1,2} C_{1,3}
C_{2,0} C_{2,1} C_{2,2} C_{2,3}
:
C_{N,0} C_{N,1} C_{N,2} C_{N,3}

-----Output-----
Print the number of the different cubes that can be constructed under the conditions.

-----Sample Input-----
6
0 1 2 3
0 4 6 1
1 6 7 2
2 7 5 3
6 4 5 7
4 0 3 5

-----Sample Output-----
1

The cube below can be constructed.
"""

from collections import Counter, defaultdict
import itertools
from functools import lru_cache

mask = (1 << 10) - 1
symmetry = defaultdict(int)

def encode(a, b, c, d):
    t = 1 << 40
    for (x, y, z, w) in [(a, b, c, d), (b, c, d, a), (c, d, a, b), (d, a, b, c)]:
        u = x + (y << 10) + (z << 20) + (w << 30)
        if t > u:
            t = u
    if a == b == c == d:
        symmetry[t] = 4
    elif a == c and b == d:
        symmetry[t] = 2
    else:
        symmetry[t] = 1
    return t

@lru_cache(None)
def decode(x):
    return [x >> n & mask for n in [0, 10, 20, 30]]

def count_possible_cubes(N, tiles):
    encoded_tiles = [encode(a, b, c, d) for (a, b, c, d) in tiles]
    counter = Counter(encoded_tiles)
    P = [(1, n, n * (n - 1), n * (n - 1) * (n - 2), n * (n - 1) * (n - 2) * (n - 3)) for n in range(N + 1)]
    P += [(0, 0, 0, 0, 0)] * (N + 1)
    power = [[n ** e for e in range(5)] for n in range(5)]
    answer = 0
    for (bottom, top) in itertools.combinations(encoded_tiles, 2):
        counter[bottom] -= 1
        counter[top] -= 1
        (a, b, c, d) = decode(bottom)
        (e, f, g, h) = decode(top)
        for (x, y, z, w) in [(e, f, g, h), (f, g, h, e), (g, h, e, f), (h, e, f, g)]:
            encoded_tiles = [encode(p, q, r, s) for (p, q, r, s) in [(b, a, x, w), (c, b, w, z), (d, c, z, y), (a, d, y, x)]]
            need = Counter(encoded_tiles)
            x = 1
            for (tile, cnt) in need.items():
                x *= P[counter[tile]][cnt]
                x *= power[symmetry[tile]][cnt]
            answer += x
        counter[bottom] += 1
        counter[top] += 1
    answer //= 3
    return answer