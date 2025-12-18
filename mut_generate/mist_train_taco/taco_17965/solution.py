"""
QUESTION:
There are N stones arranged in a row. The i-th stone from the left is painted in the color C_i.

Snuke will perform the following operation zero or more times:

* Choose two stones painted in the same color. Repaint all the stones between them, with the color of the chosen stones.



Find the number of possible final sequences of colors of the stones, modulo 10^9+7.

Constraints

* 1 \leq N \leq 2\times 10^5
* 1 \leq C_i \leq 2\times 10^5(1\leq i\leq N)
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
C_1
:
C_N


Output

Print the number of possible final sequences of colors of the stones, modulo 10^9+7.

Examples

Input

5
1
2
1
2
2


Output

3


Input

6
4
2
5
4
2
4


Output

5


Input

7
1
3
1
2
3
3
2


Output

5
"""

from collections import defaultdict

def count_possible_final_sequences(N, colors):
    mod = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    prev = defaultdict(lambda: -1)
    
    for i in range(1, N + 1):
        c = colors[i - 1]
        dp[i] = dp[i - 1]
        if prev[c] >= 0:
            if prev[c] != i - 1:
                dp[i] = (dp[i] + dp[prev[c]]) % mod
        prev[c] = i
    
    return dp[-1]