"""
QUESTION:
There is a mysterious planet called Yaen, whose space is 2-dimensional. There are many beautiful stones on the planet, and the Yaen people love to collect them. They bring the stones back home and make nice mobile arts of them to decorate their 2-dimensional living rooms.

In their 2-dimensional world, a mobile is defined recursively as follows:

* a stone hung by a string, or
* a rod of length 1 with two sub-mobiles at both ends; the rod is hung by a string at the center of gravity of sub-mobiles. When the weights of the sub-mobiles are n and m, and their distances from the center of gravity are a and b respectively, the equation n × a = m × b holds.


<image>


For example, if you got three stones with weights 1, 1, and 2, here are some possible mobiles and their widths:

<image>

Given the weights of stones and the width of the room, your task is to design the widest possible mobile satisfying both of the following conditions.

* It uses all the stones.
* Its width is less than the width of the room.



You should ignore the widths of stones.

In some cases two sub-mobiles hung from both ends of a rod might overlap (see the figure on the below). Such mobiles are acceptable. The width of the example is (1/3) + 1 + (1/4).


<image>



Input

The first line of the input gives the number of datasets. Then the specified number of datasets follow. A dataset has the following format.


r
s
w1
.
.
.
ws


r is a decimal fraction representing the width of the room, which satisfies 0 < r < 10. s is the number of the stones. You may assume 1 ≤ s ≤ 6. wi is the weight of the i-th stone, which is an integer. You may assume 1 ≤ wi ≤ 1000.

You can assume that no mobiles whose widths are between r - 0.00001 and r + 0.00001 can be made of given stones.

Output

For each dataset in the input, one line containing a decimal fraction should be output. The decimal fraction should give the width of the widest possible mobile as defined above. An output line should not contain extra characters such as spaces.

In case there is no mobile which satisfies the requirement, answer -1 instead.

The answer should not have an error greater than 0.00000001. You may output any number of digits after the decimal point, provided that the above accuracy condition is satisfied.

Example

Input

5
1.3
3
1
2
1
1.4
3
1
2
1
2.0
3
1
2
1
1.59
4
2
1
1
3
1.7143
4
1
2
3
5


Output

-1
1.3333333333333335
1.6666666666666667
1.5833333333333335
1.7142857142857142
"""

from itertools import combinations

def calculate_widest_mobile(room_width, stone_weights):
    def dfs(base, stones):
        key = tuple(stones)
        if key in rec:
            return set(((base + l, base + r) for (l, r) in rec[key]))
        edges = set()
        positions = set()
        for i in range(1, len(stones)):
            for tpl in combinations(stones, i):
                s1 = list(tpl)
                s2 = stones[:]
                for s in s1:
                    s2.remove(s)
                w1 = sum(s1)
                w2 = sum(s2)
                w = w1 + w2
                b1 = base - w2 / w
                b2 = base + w1 / w
                left_tree_ends = dfs(b1, s1)
                right_tree_ends = dfs(b2, s2)
                for (ll, lr) in left_tree_ends:
                    for (rl, rr) in right_tree_ends:
                        if ll < rl:
                            l = ll
                        else:
                            l = rl
                        if lr < rr:
                            r = rr
                        else:
                            r = lr
                        edges.add((l - base, r - base))
                        positions.add((l, r))
        rec[key] = edges
        return positions
    
    rec = dict()
    stones = sorted(stone_weights)
    for stone in stones:
        rec[stone,] = {(0, 0)}
    edge_set = dfs(0, stones)
    try:
        ans = max((b - a for (a, b) in edge_set if b - a < room_width))
        return ans
    except ValueError:
        return -1