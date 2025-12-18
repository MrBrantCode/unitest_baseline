"""
QUESTION:
Convenience store Deven Eleven is planning to open its first store in Aizuwakamatsu City to expand its business. There are already many other convenience stores in Aizuwakamatsu, so the place to open a new store is likely to be the key to success. Under the premise that "customers use the convenience store closest to the area where they live," Seven Eleven has decided to open a store at "a point that many customers will use."

| <image>
--- | ---

Seven Eleven has divided the map of Aizuwakamatsu City using a congruent regular hexagon (hereinafter referred to as "block") in order to grasp the range covered by each existing convenience store. At this time, each block was divided so that there was at most one existing convenience store. On this map, the distance to the convenience store is calculated based on the number of blocks that go through from each block to the convenience store. We believe that each block is covered by the convenience store with the shortest distance. The problem is to look for "a block without an existing convenience store that covers as many blocks as possible" based on this map.

As a Deven-Eleven programmer, you have decided to develop a program that calculates the number of blocks that can be covered most widely from the block-divided map information and the information on the candidate sites for new stores.

The map divided into m x n is shown as shown in Fig. 1. There are m hexagonal blocks horizontally and n vertically, each represented by one coordinate (x, y). The left edge of the odd row is located at the bottom left of the left edge of the row above it, and the left edge of the even row is located at the bottom right of the left edge of the row above it. For example, the coordinates (1, 1) indicate the upper left block in Figure 1. Also, the coordinates (1, 2) are located at the lower right of the coordinates (1, 1), and the coordinates (1, 3) are located at the lower left of the coordinates (1, 2).

<image>


Figure 2 shows an example of the case where there are 6 existing convenience stores, which are divided into 6 x 6. Each convenience store is numbered in order from 1. At this time, if the blocks covered by each convenience store are painted separately for each number, it will be as shown in Fig. 3. Unpainted blocks such as coordinates (1, 4) and (2, 5) have two or more closest convenience stores, and neither is a block that can be judged. For example, in the case of a block with coordinates (1, 4), the distance to the convenience store number 4 and the convenience store number 5 are equal, and it is assumed that no convenience store covers this block. The number of blocks covered by the convenience store number 4 is 5.

<image>


Now suppose that Seven Eleven considers coordinates (1, 3) and coordinates (5, 3) as potential sites for a new store. If you set up a store at coordinates (1, 3), the number of blocks that can be covered is 3 (Fig. 4). On the other hand, if you set up a store at coordinates (5, 3), the number of blocks that can be covered is 4 (Fig. 5). Therefore, the number of blocks that can be covered most widely is 4.

<image>


Enter map information m x n, number of existing convenience stores s and their coordinates (x, y), number of candidate sites t and their coordinates (p, q), and the number of blocks that can be covered most widely among all candidate sites. Create a program that outputs.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by two lines of zeros. Each dataset is given in the following format:


m n
s
x1 y1
x2 y2
::
xs ys ys
t
p1 q1
p2 q2
::
pt qt


The integers m, n (2 ≤ m, n ≤ 100) are given to represent the size (horizontal, vertical) of the divided map on the first line.

The second line gives the number of existing convenience stores s (1 ≤ s ≤ 10). The following s line is given the coordinates xi, y1 of the ith existing convenience store.

The next line is given the number of potential new store sites t (1 ≤ t ≤ 10). The following t line is given the coordinates pi, qi of the i-th candidate site.

The number of datasets does not exceed 20.

Output

For each data set, the number of blocks that can cover the widest of all candidate sites is output on one line.

Example

Input

6 6
6
1 1
6 1
3 2
3 5
1 6
5 6
2
1 3
5 3
6 6
6
3 2
3 5
6 1
1 1
1 6
5 6
2
2 3
5 3
0 0


Output

4
4
"""

def generate_next_hexes(x, y):
    hexes = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
    if y % 2:
        hexes += [(x - 1, y - 1), (x - 1, y + 1)]
    else:
        hexes += [(x + 1, y - 1), (x + 1, y + 1)]
    return hexes

def update_map(hex_map, hexes, m, n):
    num_updated_hexes = 0
    distance = 0
    while hexes:
        next_hexes = []
        for pos in hexes:
            x = pos[0]
            y = pos[1]
            if 1 <= x <= m and 1 <= y <= n and (pos not in hex_map or distance < hex_map[pos]):
                hex_map[pos] = distance
                num_updated_hexes += 1
                next_hexes += generate_next_hexes(x, y)
        distance += 1
        hexes = next_hexes
    return num_updated_hexes

def calculate_max_coverage(m, n, existing_stores, candidate_sites):
    hex_map = {}
    update_map(hex_map, existing_stores, m, n)
    
    max_num_blocks = 0
    for candidate in candidate_sites:
        new_hex_map = hex_map.copy()
        num_blocks = update_map(new_hex_map, [candidate], m, n)
        max_num_blocks = max(max_num_blocks, num_blocks)
    
    return max_num_blocks