"""
QUESTION:
There are N rabbits on a number line. The rabbits are conveniently numbered 1 through N. The coordinate of the initial position of rabbit i is x_i.

The rabbits will now take exercise on the number line, by performing sets described below. A set consists of M jumps. The j-th jump of a set is performed by rabbit a_j (2≤a_j≤N-1). For this jump, either rabbit a_j-1 or rabbit a_j+1 is chosen with equal probability (let the chosen rabbit be rabbit x), then rabbit a_j will jump to the symmetric point of its current position with respect to rabbit x.

The rabbits will perform K sets in succession. For each rabbit, find the expected value of the coordinate of its eventual position after K sets are performed.

Constraints

* 3≤N≤10^5
* x_i is an integer.
* |x_i|≤10^9
* 1≤M≤10^5
* 2≤a_j≤N-1
* 1≤K≤10^{18}

Input

The input is given from Standard Input in the following format:


N
x_1 x_2 ... x_N
M K
a_1 a_2 ... a_M


Output

Print N lines. The i-th line should contain the expected value of the coordinate of the eventual position of rabbit i after K sets are performed. The output is considered correct if the absolute or relative error is at most 10^{-9}.

Examples

Input

3
-1 0 2
1 1
2


Output

-1.0
1.0
2.0


Input

3
1 -1 1
2 2
2 2


Output

1.0
-1.0
1.0


Input

5
0 1 3 6 10
3 10
2 3 4


Output

0.0
3.0
7.0
8.0
10.0
"""

def calculate_expected_positions(N, x, M, K, a):
    b = []
    x2 = []
    c = []
    
    # Initialize b and x2
    for i in range(1, N):
        b.append(i - 1)
        x2.append(x[i] - x[i - 1])
    
    # Process the jumps
    for i in range(M):
        to = a[i] - 1
        b[to], b[to - 1] = b[to - 1], b[to]
    
    # Initialize c
    c = [-1] * (N - 1)
    for i in range(N - 1):
        c[b[i]] = i
    
    # Perform the sets
    for i in range(60):
        x3 = [0] * (N - 1)
        if K & (1 << i):
            for j in range(N - 1):
                x3[c[j]] = x2[j]
            x2 = x3
        c2 = [-1] * (N - 1)
        for j in range(N - 1):
            c2[j] = c[c[j]]
        c = c2
    
    # Calculate the final positions
    s = x[0]
    result = [s]
    for i in x2:
        s += i
        result.append(s)
    
    return result