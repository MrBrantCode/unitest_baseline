"""
QUESTION:
During the Steam Summer Sale, Jim's $N-1$ friends have purchased $\mbox{M}$ games, which are numbered from $\mbox{1}$ to $\mbox{M}$. The games are multiplayer. Jim has invited his friends to his basement where they will play by making a LAN-Party. 

Each friend has already decided the game he would like to play for the rest of the day. So there will be a group of friends who will play the same game together.

But then, they face a problem: Currently, none of the friends' PCs are connected. So they have to be connected using the available $\mbox{Q}$ wires. Jim decides to connect friends $u_i$ and $v_i$ with the $\boldsymbol{i}^{th}$ wire one by one. So he starts with wire 1, then with wire 2 and so on. 

A group can start playing their game, only if all the members are connected (if not directly, then there must exist a path connecting them). They want to start playing as soon as possible. 

For each game, find out the wire after adding which the group can start playing. It is also possible that a group will never get connected. In such a case, this group starts crying and you should display -1.

Input Format

On the first line there will be $N$, $\mbox{M}$ and $\mbox{Q}$ each separated by a single space. On the second line we will give you $N$ integers separated by a single space: The $\boldsymbol{i}$-th integer denotes the game friend $\boldsymbol{i}$ wants to play (all between $\mbox{1}$ and $\mbox{M}$). The next $\mbox{Q}$ lines will denote $\mbox{Q}$ wires: $i^{th}$ line denotes $i^{th}$ wire and is denoted by $u_i$ and $v_i$ pairs each separated by a single space. 

Constraints

$1\leq N,M\leq10^5$ For each game $\boldsymbol{i}$, the number of players playing $\boldsymbol{i}$ will be positive. 

$0\leq Q\leq10^5$  

Note
Each game is chosen by at least one player. If a group consists of only one member, then print 0, since this lucky (?) lone player can start right away!

Output Format

Print on the $\boldsymbol{i}^{th} $line the answer for the $\boldsymbol{i}^{th} $game. 

Sample Input
5 2 4
1 2 2 2 1
1 2 
2 3
1 5
4 5 

Sample Output
3
4

Explanation

The group with the game 1 can play after the 3^{rd} wire is added. The group with game 2 can play only after the 4^{th} wire has been added because after adding the 4^{th} wire, a path between (2,3) (3,4) and (2,4) gets created.
"""

class Vertex:
    def __init__(self, i, c, cc):
        self.i = i
        self.c = c
        self.cc = cc
        self.e = []

def merge_cc(cc, v, i, j, res, n, color_counts):
    to_rem = j if len(cc[i][1]) > len(cc[j][1]) else i
    to_leave = j if to_rem == i else i
    cc[to_rem][2] = False
    for i in cc[to_rem][1]:
        v[i].cc = to_leave
        cc[to_leave][1].append(i)
        if v[i].c in cc[to_leave][0]:
            cc[to_leave][0][v[i].c] += 1
        else:
            cc[to_leave][0][v[i].c] = 1
        if cc[to_leave][0][v[i].c] == color_counts[v[i].c] and res[v[i].c] == -1:
            res[v[i].c] = n
    cc[to_rem][1] = []

def find_game_start_wires(n, m, q, colors, wires):
    vs = []
    comps = {}
    color_counts = {}
    res = {}

    for i in range(n):
        vs.append(Vertex(i, colors[i], i))
        comps[i] = [{colors[i]: 1}, [i], True]
        if colors[i] in color_counts:
            color_counts[colors[i]] += 1
        else:
            color_counts[colors[i]] = 1

    for c in set(colors):
        res[c] = -1

    for c in color_counts:
        if color_counts[c] == 1:
            res[c] = 0

    for i in range(q):
        a, b = wires[i]
        a -= 1
        b -= 1
        vs[a].e.append(b)
        vs[b].e.append(a)
        if vs[a].cc != vs[b].cc:
            merge_cc(comps, vs, vs[a].cc, vs[b].cc, res, i + 1, color_counts)

    result = [res[i] for i in sorted(res.keys())]
    return result