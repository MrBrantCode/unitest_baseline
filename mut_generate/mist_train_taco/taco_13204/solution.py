"""
QUESTION:
A pitch-black room

When I woke up, Mr. A was in a pitch-black room. Apparently, Mr. A got lost in a dungeon consisting of N rooms. You couldn't know which room A got lost in, but fortunately he got a map of the dungeon. Let's show A the way to go and lead to a bright room.

It is known that M of the N rooms are pitch black, and the D_1, D_2, ..., and D_Mth rooms are pitch black, respectively. Also, there are exactly K one-way streets from all the rooms in order, and the roads from the i-th room are v_ {i, 1}, v_ {i, 2}, ..., v_ {i, respectively. , K} Connected to the third room. You can follow the a_1, a_2, ..., a_lth roads in order from the room you are in for Mr. A. However, when Mr. A reaches the bright room, he ignores the subsequent instructions. You cannot know the information of the room where Mr. A is currently before and after the instruction, so you must give the instruction sequence so that you can reach the bright room no matter which room you are in. Answer the length of the shortest of such instructions.

Constraints

* 2 ≤ N ≤ 100
* 1 ≤ M ≤ min (16, N − 1)
* 1 ≤ K ≤ N
* 1 ≤ D_i ≤ N
* D_i are all different
* 1 ≤ v_ {i, j} ≤ N
* All dark rooms can reach at least one bright room



Input Format

Input is given from standard input in the following format.


NMK
D_1 D_2 ... D_M
v_ {1,1} v_ {1,2} ... v_ {1,K}
v_ {2,1} v_ {2,2} ... v_ {2, K}
...
v_ {N, 1} v_ {N, 2} ... v_ {N, K}


Output Format

Print the answer in one line.

Sample Input 1


4 2 2
1 2
twenty four
3 1
4 2
13


Sample Output 1


2


<image>
If you give the instruction 1, 1

* If A's initial position is room 1, the second move will reach room 3.
* If A's initial position is room 2, the first move will reach room 3.



Sample Input 2


3 2 2
1 2
twenty three
1 2
twenty one


Sample Output 2


3


<image>
If you give instructions 2, 1, 2

* If A's initial position is room 1, the first move will reach room 3.
* If A's initial position is room 2, the third move will reach room 3.



Sample Input 3


6 3 3
one two Three
4 1 1
2 5 2
3 3 6
4 4 4
5 5 5
6 6 6


Sample Output 3


3


<image>
Beware of unconnected cases and cases with self-edges and multiple edges.





Example

Input

4 2 2
1 2
2 4
3 1
4 2
1 3


Output

2
"""

import collections

def find_shortest_instruction_length(n, m, k, dark_rooms, connections):
    dd = collections.defaultdict(lambda: None)
    for i in range(m):
        dd[dark_rooms[i]] = i
    
    ii = [2 ** _ for _ in range(m)]
    vv = [[ii[dd[connections[c][i]]] if not dd[connections[c][i]] is None else 0 for c in dark_rooms] for i in range(k)]
    
    m2 = 2 ** m
    u = [None] * m2
    u[-1] = 1
    q = [m2 - 1]
    r = 0
    
    while q:
        r += 1
        nq = []
        for qd in q:
            qdi = [di for di in range(m) if qd & ii[di]]
            for vi in range(k):
                t = 0
                vvi = vv[vi]
                for di in qdi:
                    t |= vvi[di]
                if not u[t] is None:
                    continue
                if t == 0:
                    return r
                u[t] = 1
                nq.append(t)
        q = nq
    
    return -1