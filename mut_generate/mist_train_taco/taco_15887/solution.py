"""
QUESTION:
There are N blocks, numbered 1, 2, \ldots, N. For each i (1 \leq i \leq N), Block i has a weight of w_i, a solidness of s_i and a value of v_i.

Taro has decided to build a tower by choosing some of the N blocks and stacking them vertically in some order. Here, the tower must satisfy the following condition:

* For each Block i contained in the tower, the sum of the weights of the blocks stacked above it is not greater than s_i.



Find the maximum possible sum of the values of the blocks contained in the tower.

Constraints

* All values in input are integers.
* 1 \leq N \leq 10^3
* 1 \leq w_i, s_i \leq 10^4
* 1 \leq v_i \leq 10^9

Input

Input is given from Standard Input in the following format:


N
w_1 s_1 v_1
w_2 s_2 v_2
:
w_N s_N v_N


Output

Print the maximum possible sum of the values of the blocks contained in the tower.

Examples

Input

3
2 2 20
2 1 30
3 1 40


Output

50


Input

4
1 2 10
3 1 10
2 4 10
1 6 10


Output

40


Input

5
1 10000 1000000000
1 10000 1000000000
1 10000 1000000000
1 10000 1000000000
1 10000 1000000000


Output

5000000000


Input

8
9 5 7
6 2 7
5 7 3
7 8 8
1 9 6
3 3 3
4 1 7
4 5 5


Output

22
"""

def max_tower_value(blocks):
    # Sort blocks by the sum of weight and solidness
    blocks.sort(key=lambda x: x[0] + x[1])
    
    # Define the maximum possible sum of weights and solidness
    max_s = 10 ** 4
    
    # Initialize DP array with negative infinity
    DP = [-float('inf')] * (2 * max_s + 1)
    DP[0] = 0
    
    # Iterate over each block
    for w, s, v in blocks:
        nxt = DP[:]
        for j in range(s + 1):
            nxt[j + w] = max(DP[j] + v, nxt[j + w])
        DP = nxt
    
    # The answer is the maximum value in the DP array
    return max(DP)