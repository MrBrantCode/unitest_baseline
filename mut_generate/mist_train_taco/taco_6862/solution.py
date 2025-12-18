"""
QUESTION:
We have a rooted binary tree with N vertices, where the vertices are numbered 1 to N. Vertex 1 is the root, and the parent of Vertex i (i \geq 2) is Vertex \left[ \frac{i}{2} \right].

Each vertex has one item in it. The item in Vertex i has a value of V_i and a weight of W_i. Now, process the following query Q times:

* Given are a vertex v of the tree and a positive integer L. Let us choose some (possibly none) of the items in v and the ancestors of v so that their total weight is at most L. Find the maximum possible total value of the chosen items.



Here, Vertex u is said to be an ancestor of Vertex v when u is an indirect parent of v, that is, there exists a sequence of vertices w_1,w_2,\ldots,w_k (k\geq 2) where w_1=v, w_k=u, and w_{i+1} is the parent of w_i for each i.

Constraints

* All values in input are integers.
* 1 \leq N < 2^{18}
* 1 \leq Q \leq 10^5
* 1 \leq V_i \leq 10^5
* 1 \leq W_i \leq 10^5
* For the values v and L given in each query, 1 \leq v \leq N and 1 \leq L \leq 10^5.

Input

Let v_i and L_i be the values v and L given in the i-th query. Then, Input is given from Standard Input in the following format:


N
V_1 W_1
:
V_N W_N
Q
v_1 L_1
:
v_Q L_Q


Output

For each integer i from 1 through Q, the i-th line should contain the response to the i-th query.

Examples

Input

3
1 2
2 3
3 4
3
1 1
2 5
3 5


Output

0
3
3


Input

15
123 119
129 120
132 112
126 109
118 103
115 109
102 100
130 120
105 105
132 115
104 102
107 107
127 116
121 104
121 115
8
8 234
9 244
10 226
11 227
12 240
13 237
14 206
15 227


Output

256
255
250
247
255
259
223
253
"""

def max_possible_value(N, values, weights, queries):
    MX = 10 ** 5
    H = min(N + 1, 1 << 10)
    dp = [None] * H
    dp[0] = [0] * (MX + 1)
    IV = []
    IW = []
    
    for i in range(1, N + 1):
        v = values[i - 1]
        w = weights[i - 1]
        if i < H:
            dpi = dp[i >> 1][:]
            dp[i] = dpi
            for j in range(MX, w - 1, -1):
                dpi[j] = max(dpi[j], dpi[j - w] + v)
        else:
            IV.append(v)
            IW.append(w)
    
    results = []
    for (v, L) in queries:
        if v < H:
            results.append(dp[v][L])
            continue
        item_values = []
        item_weights = []
        while v >= H:
            item_values.append(IV[v - H])
            item_weights.append(IW[v - H])
            v >>= 1
        l = len(item_values)
        V = [0] * (1 << l)
        W = [0] * (1 << l)
        ans = dp[v][L]
        for i in range(1, 1 << l):
            msb = i & -i
            msbb = msb.bit_length() - 1
            wi = W[i - msb] + item_weights[msbb]
            W[i] = wi
            if wi <= L:
                vi = V[i - msb] + item_values[msbb]
                ans = max(ans, vi + dp[v][L - wi])
                V[i] = vi
        results.append(ans)
    
    return results