"""
QUESTION:
Snuke has a blackboard and a set S consisting of N integers. The i-th element in S is S_i.

He wrote an integer X on the blackboard, then performed the following operation N times:

* Choose one element from S and remove it.
* Let x be the number written on the blackboard now, and y be the integer removed from S. Replace the number on the blackboard with x \bmod {y}.



There are N! possible orders in which the elements are removed from S. For each of them, find the number that would be written on the blackboard after the N operations, and compute the sum of all those N! numbers modulo 10^{9}+7.

Constraints

* All values in input are integers.
* 1 \leq N \leq 200
* 1 \leq S_i, X \leq 10^{5}
* S_i are pairwise distinct.

Input

Input is given from Standard Input in the following format:


N X
S_1 S_2 \ldots S_{N}


Output

Print the answer.

Examples

Input

2 19
3 7


Output

3


Input

5 82
22 11 6 5 13


Output

288


Input

10 100000
50000 50001 50002 50003 50004 50005 50006 50007 50008 50009


Output

279669259
"""

def compute_blackboard_sum(N, X, S, MOD=10**9 + 7):
    memo = [{} for _ in range(N)]
    S.sort(reverse=True)

    def ddp(cur_N, cur_x):
        if cur_N == N:
            return cur_x
        if cur_x in memo[cur_N]:
            return memo[cur_N][cur_x]
        ret = ddp(cur_N + 1, cur_x % S[cur_N]) + ddp(cur_N + 1, cur_x) * (N - cur_N - 1)
        ret = ret % MOD
        memo[cur_N][cur_x] = ret
        return ret
    
    return ddp(0, X)