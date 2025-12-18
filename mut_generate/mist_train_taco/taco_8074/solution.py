"""
QUESTION:
Consider the following game:

* The game is played using a row of N squares and many stones.
* First, a_i stones are put in Square i\ (1 \leq i \leq N).
* A player can perform the following operation as many time as desired: "Select an integer i such that Square i contains exactly i stones. Remove all the stones from Square i, and add one stone to each of the i-1 squares from Square 1 to Square i-1."
* The final score of the player is the total number of the stones remaining in the squares.



For a sequence a of length N, let f(a) be the minimum score that can be obtained when the game is played on a.

Find the sum of f(a) over all sequences a of length N where each element is between 0 and K (inclusive). Since it can be extremely large, find the answer modulo 1000000007 (= 10^9+7).

Constraints

* 1 \leq N \leq 100
* 1 \leq K \leq N

Input

Input is given from Standard Input in the following format:


N K


Output

Print the sum of f(a) modulo 1000000007 (= 10^9+7).

Examples

Input

2 2


Output

10


Input

20 17


Output

983853488
"""

def calculate_minimum_score_sum(N, K, mod=10**9 + 7):
    lis = [0] * 3300
    lis[0] = 1
    
    for i in range(N, 0, -1):
        nlis = [0] * 3300
        for j in range(K + 1):
            for last in range(3300):
                if i < j:
                    nlis[last] += lis[last]
                    nlis[last] %= mod
                elif (last + j) // i + last < 3300:
                    nlis[last + (last + j) // i] += lis[last]
                    nlis[last + (last + j) // i] %= mod
        lis = nlis
    
    ans = K * (K + 1) // 2 * pow(K + 1, N - 1, mod) * N
    for i in range(3300):
        ans -= lis[i] * i
        ans %= mod
    
    return ans