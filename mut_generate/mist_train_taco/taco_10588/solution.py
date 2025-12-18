"""
QUESTION:
You are given an integer N. Determine if there exists a tree with 2N vertices numbered 1 to 2N satisfying the following condition, and show one such tree if the answer is yes.

* Assume that, for each integer i between 1 and N (inclusive), Vertex i and N+i have the weight i. Then, for each integer i between 1 and N, the bitwise XOR of the weights of the vertices on the path between Vertex i and N+i (including themselves) is i.

Constraints

* N is an integer.
* 1 \leq N \leq 10^{5}

Input

Input is given from Standard Input in the following format:


N


Output

If there exists a tree satisfying the condition in the statement, print `Yes`; otherwise, print `No`. Then, if such a tree exists, print the 2N-1 edges of such a tree in the subsequent 2N-1 lines, in the following format:


a_{1} b_{1}
\vdots
a_{2N-1} b_{2N-1}


Here each pair (a_i, b_i) means that there is an edge connecting Vertex a_i and b_i. The edges may be printed in any order.

Examples

Input

3


Output

Yes
1 2
2 3
3 4
4 5
5 6


Input

1


Output

No
"""

def find_tree_with_xor_property(N: int) -> tuple:
    if N == 1:
        return (False, None)
    elif N % 2 == 1:
        edges = []
        for i in range(2, N + 1, 2):
            edges.append((1, i))
            edges.append((i, i + 1))
            edges.append((1, i + 1 + N))
            edges.append((i + 1 + N, i + N))
        edges.append((N + 1, 3))
        return (True, edges)
    else:
        a = None
        b = None
        for i in range(1, N):
            if N ^ i < N:
                a = i
                b = N ^ i
        if a is None:
            return (False, None)
        
        edges = []
        for i in range(2, N, 2):
            edges.append((i, i + 1))
            edges.append((N + i, N + i + 1))
            if i not in (a, b) and i + 1 not in (a, b):
                edges.append((1, i))
                edges.append((1, N + i + 1))
        
        pa = a ^ 1
        pb = b ^ 1
        edges.append((N + 1, a))
        edges.append((a, b))
        edges.append((N, a))
        edges.append((b, 2 * N))
        edges.append((1, pa))
        edges.append((1, a + N))
        edges.append((pa + N, pb + N))
        
        return (True, edges)